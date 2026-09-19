"""Deterministic regression tests. No paid APIs, provider writes or model calls."""
from __future__ import annotations
import ast
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import types
from unittest.mock import Mock
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'marketing/scripts'))
from lib import credentials, http_cache, dataforseo_client as dfs


def load(relative):
    path = ROOT / relative
    name = 'test_module_' + path.stem.replace('-', '_')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


power = load('data-science/scripts/power-calc.py')
cvp = load('economics/scripts/cvp-calc.py')
cba = load('economics/skills/cost-benefit-analysis-framework/scripts/cba-calculator.py')
cohort = load('data-science/skills/cohort-analysis-builder/scripts/cohort-query-builder.py')
threshold = load('data-science/skills/anomaly-detection-rule-builder/scripts/validate-thresholds.py')
pipeline = load('data-science/skills/data-pipeline-architecture/scripts/pipeline-validator.py')
tokens = load('marketing/skills/design-tokens/scripts/token-converter.py')
workspace = load('startups/scripts/venture_workspace.py')
retention = load('startups/scripts/retention_model.py')
setup = load('marketing/scripts/setup_environment.py')
portability = load('scripts/check-portability.py')


@pytest.mark.parametrize('value', [0, 1, -1, float('nan'), float('inf')])
def test_z_probability_rejects_invalid(value):
    with pytest.raises(ValueError): power.z_score(value)


def test_z_accuracy_and_power_monotonicity():
    assert power.z_score(.975) == pytest.approx(1.95996398454)
    assert power.sample_size_proportions(.1, .005, .05, .8, True) > power.sample_size_proportions(.1, .01, .05, .8, True)


@pytest.mark.parametrize('args', [(.9,.2,.05,.8), (.1,0,.05,.8), (.1,.1,0,.8), (.1,.1,.05,.4), (float('nan'),.1,.05,.8)])
def test_power_input_validation(args):
    with pytest.raises(ValueError): power.sample_size_proportions(*args, True)


def test_break_even_ceil_not_round():
    result = cvp.compute(100, 1, 4, 2)
    assert result['break_even_units'] == 34
    assert result['target_units'] == 34
    assert result['break_even_units_exact'] == pytest.approx(100/3)


@pytest.mark.parametrize('args', [(-1,1,4), (100,-1,4), (100,4,4), (100,1,float('inf'))])
def test_break_even_invalid(args):
    assert 'error' in cvp.compute(*args)


def test_cba_does_not_invent_gross_bcr():
    result = cba.evaluate_option('Example', [-100, -50, 200], 0)
    assert result['npv'] == 50
    assert result['profitability_index'] == 1.5
    assert result['net_flow_ratio'] == pytest.approx(1.3333)
    assert result['benefit_cost_ratio'] is None


def test_cba_known_irr_and_endpoint_and_payback():
    assert cba.irr([-100, 110]) == pytest.approx(.1, abs=1e-6)
    assert cba.irr([-100,1100]) == 10
    assert cba.payback([100, -50]) == 0
    assert cba.discounted_payback(.1, [100, -50]) == 0
    assert cba.payback([-100,50,100]) == 1.5


@pytest.mark.parametrize('rate,flows', [(-1,[-100,110]), (float('nan'),[-100,110]), (.1,[]), (.1,[-100,float('inf')])])
def test_cba_invalid(rate, flows):
    with pytest.raises(ValueError): cba.evaluate_option('x', flows, rate)


def test_retention_not_churn_survival():
    result = retention.retention_model(.94)
    assert result['cohort_remaining'] == pytest.approx(.94**12)
    assert result['average_lifetime_months'] == pytest.approx(1/.06)
    assert retention.retention_model(1)['average_lifetime_months'] is None
    assert retention.retention_model(0)['average_lifetime_months'] == 1


@pytest.mark.parametrize('r,months', [(-.1,12), (1.1,12), (float('nan'),12), (.9,-1), (.9,1.5), (.9,True)])
def test_retention_boundaries(r, months):
    with pytest.raises(ValueError): retention.retention_model(r, months)


def test_workspace_idempotent_and_preserves_work(tmp_path):
    first = workspace.initialise(tmp_path, 'example')
    root = Path(first['workspace'])
    assert len(first['created']) == 6
    (root/'00-vision/vision-sketch.md').write_text('user content')
    log = (root/'log.md').read_text()
    second = workspace.initialise(tmp_path, 'example')
    assert second['created'] == []
    assert (root/'00-vision/vision-sketch.md').read_text() == 'user content'
    assert (root/'log.md').read_text() == log
    assert workspace.resolve_workspace(tmp_path) == root
    assert workspace.resolve_workspace(tmp_path, 'example') == root


@pytest.mark.parametrize('slug', ['../elsewhere','A','a/b','a--b','', 'a b'])
def test_workspace_rejects_unsafe_slugs(tmp_path, slug):
    with pytest.raises(ValueError): workspace.initialise(tmp_path, slug)


def test_workspace_refuses_unrelated_directory(tmp_path):
    root = tmp_path/'.project/plans/startups/example'
    root.mkdir(parents=True); (root/'precious.md').write_text('keep')
    with pytest.raises(ValueError): workspace.initialise(tmp_path,'example')
    assert (root/'precious.md').read_text() == 'keep'


def test_workspace_resume_profile_and_missing_artifacts(tmp_path):
    root = tmp_path/'.project/plans/startups/example'; root.mkdir(parents=True)
    (root/'venture.json').write_text('{"profile":"venture","name":"example"}')
    result = workspace.initialise(tmp_path,'example')
    assert 'venture.json' in result['preserved']
    assert len(result['created']) == 5


def test_workspace_ambiguous_and_legacy(tmp_path):
    workspace.initialise(tmp_path, 'one'); workspace.initialise(tmp_path, 'two')
    with pytest.raises(ValueError): workspace.resolve_workspace(tmp_path)
    legacy = tmp_path/'legacy'; legacy.mkdir()
    (legacy/'memex.config.json').write_text('{"profile":"venture"}')
    (legacy/'.memex').mkdir()
    assert workspace.resolve_workspace(legacy) == legacy/'.memex'


def test_workspace_symlink_escape(tmp_path):
    other = tmp_path/'outside'; other.mkdir()
    project = tmp_path/'project'; project.mkdir()
    (project/'.project').symlink_to(other, target_is_directory=True)
    with pytest.raises(ValueError): workspace.initialise(project,'example')
    assert list(other.iterdir()) == []


@pytest.fixture
def credential_file(tmp_path, monkeypatch):
    file = tmp_path/'credentials.json'
    monkeypatch.setenv('SEO_CREDENTIALS_FILE', str(file))
    return file


def test_credentials_reload_and_env_override(credential_file, monkeypatch):
    credential_file.write_text('{"x":{"key":"one"}}')
    assert credentials.get_credential('x','key') == 'one'
    credential_file.write_text('{"x":{"key":"two"}}')
    assert credentials.get_credential('x','key') == 'two'
    monkeypatch.setenv('TEST_API_KEY','environment')
    assert credentials.get_credential('x','key','TEST_API_KEY') == 'environment'


@pytest.mark.parametrize('value', ['[]','null','{"x":1}','{"x":{"key":12}}','{bad'])
def test_credentials_bad_shapes(credential_file, value):
    credential_file.write_text(value)
    with pytest.raises(ValueError): credentials.load_credentials()


def test_credentials_explicit_missing_does_not_fall_back(credential_file, tmp_path, monkeypatch):
    (tmp_path/'fallback').mkdir(); (tmp_path/'fallback/credentials.json').write_text('{"x":{"key":"wrong"}}')
    monkeypatch.setenv('PLUGIN_DATA',str(tmp_path/'fallback'))
    assert credentials.get_credential('x','key') is None


def test_native_data_variable_has_precedence(tmp_path, monkeypatch):
    monkeypatch.delenv('SEO_CREDENTIALS_FILE',raising=False)
    monkeypatch.setenv('PLUGIN_DATA',str(tmp_path)); monkeypatch.setenv('CLAUDE_PLUGIN_DATA',str(tmp_path/'legacy'))
    (tmp_path/'credentials.json').write_text('{"x":{"key":"native"}}')
    assert credentials.get_credential('x','key') == 'native'
    assert setup.data_dir() == tmp_path


def mock_client(monkeypatch, module, *, data=None, text=''):
    response = Mock(); response.json.return_value=data; response.text=text
    client = Mock(); client.get.return_value=response; client.post.return_value=response
    context = Mock(); context.__enter__=Mock(return_value=client); context.__exit__=Mock(return_value=False)
    monkeypatch.setattr(module.httpx,'Client',Mock(return_value=context))
    return client


def test_cache_account_and_parameter_isolation():
    key = http_cache._cache_key
    assert key('url', {'a':'1&b=2'}) != key('url', {'a':'1','b':'2'})
    assert key('url', {}, {'Authorization':'a'}) != key('url',{}, {'Authorization':'b'})
    assert key('url', {'a':1,'b':2}) == key('url', {'b':2,'a':1})
    assert key('url', {}, {'Authorization':'a'}) == key('url',{}, {'authorization':'a'})


def test_cache_hit_corrupt_and_zero_ttl(tmp_path, monkeypatch):
    monkeypatch.setenv('PLUGIN_DATA',str(tmp_path))
    client = mock_client(monkeypatch,http_cache,data={'ok':True})
    assert http_cache.cached_get('https://example.test') == {'ok':True}
    assert http_cache.cached_get('https://example.test') == {'ok':True}
    assert client.get.call_count == 1
    next((tmp_path/'cache').glob('*.json')).write_text('not json')
    http_cache.cached_get('https://example.test'); assert client.get.call_count == 2
    http_cache.cached_get('https://example.test',ttl_hours=0); assert client.get.call_count == 3


def test_cache_unwritable_directory_does_not_hide_response(monkeypatch):
    monkeypatch.setattr(http_cache,'_cache_dir',Mock(side_effect=OSError('readonly')))
    mock_client(monkeypatch,http_cache,data={'ok':True})
    assert http_cache.cached_get('https://example.test') == {'ok':True}


@pytest.mark.parametrize('ttl', [-1,float('inf'),float('nan')])
def test_cache_rejects_invalid_ttl(ttl):
    with pytest.raises(ValueError): http_cache.cached_get('unused', ttl_hours=ttl)


def test_dataforseo_correct_payload_and_direct_results(monkeypatch):
    post=Mock(return_value=[{'result':[{'keyword':'one'},{'keyword':'two'}]}])
    monkeypatch.setattr(dfs,'_post',post)
    assert dfs.keyword_suggestions('seed',limit=1) == [{'keyword':'one'}]
    payload=post.call_args.args[1][0]
    assert payload['keywords'] == ['seed']
    assert 'keyword' not in payload and 'limit' not in payload


@pytest.mark.parametrize('body', [{'status_code':40000}, {'status_code':20000,'tasks':[]}, {'status_code':20000,'tasks':[{'status_code':40000}]}, {'status_code':20000,'tasks':[{'status_code':20000,'result':{}}]}])
def test_dataforseo_errors_not_zero_volume(body, monkeypatch):
    monkeypatch.setattr(dfs,'_get_auth_header',lambda:'Basic fake')
    mock_client(monkeypatch,dfs,data=body)
    with pytest.raises(RuntimeError): dfs._post('unused',[])


def test_empty_keyword_batch_does_not_make_paid_call(monkeypatch):
    post=Mock(); monkeypatch.setattr(dfs,'_post',post)
    assert dfs.keyword_volume([]) == []
    post.assert_not_called()


@pytest.mark.parametrize('strategy', ['mobile','desktop'])
def test_lighthouse_real_supported_arguments(strategy,tmp_path,monkeypatch):
    fake=tmp_path/'lighthouse'; fake.write_text('#!/usr/bin/env python3\nimport json,sys\nprint(json.dumps(sys.argv[1:]))\n'); fake.chmod(0o755)
    monkeypatch.setenv('LIGHTHOUSE_BIN',str(fake))
    result=subprocess.run(['bash',str(ROOT/'marketing/scripts/lighthouse_runner.sh'),'https://example.test','--strategy',strategy],capture_output=True,text=True,timeout=10)
    assert result.returncode == 0, result.stderr
    args=json.loads(result.stdout)
    assert '--strategy' not in args and '--no-sandbox' not in ' '.join(args)
    assert ('--preset=desktop' in args) == (strategy=='desktop')


@pytest.mark.parametrize('args',[[],['not-a-url'],['https://example.test','--strategy'],['https://example.test','--strategy','invalid']])
def test_lighthouse_bad_arguments(args):
    result=subprocess.run(['bash',str(ROOT/'marketing/scripts/lighthouse_runner.sh'),*args],capture_output=True,timeout=10)
    assert result.returncode == 2


def test_even_median_and_no_unlabelled_false_positive_claim(capsys):
    threshold.validate([1,2,3,8],upper=2,lower=None)
    output=capsys.readouterr().out
    assert 'Median: 2.50' in output
    assert 'false-positive rate' not in output.lower()


@pytest.mark.parametrize('values,upper,lower',[([],1,None),([float('nan')],1,None),([1,2],1,2),([1],float('inf'),None)])
def test_threshold_invalid(values,upper,lower):
    with pytest.raises(ValueError): threshold.validate(values,upper,lower)


def test_pipeline_disabled_config_does_not_count_as_enabled():
    findings=pipeline.validate({'steps':[{'name':'extract'}],'retry':False,'monitoring':False,'idempotent':False})
    assert any('No error handling' in f['message'] for f in findings)
    assert any('No monitoring' in f['message'] for f in findings)
    assert any('No idempotency' in f['message'] for f in findings)


@pytest.mark.parametrize('spec',[None,[],42,{'steps':'invalid'},{'steps':[42]}])
def test_pipeline_bad_shapes_have_errors(spec):
    assert any(f['severity']=='ERROR' for f in pipeline.validate(spec))


def test_tokens_dimension_and_legacy_type():
    assert tokens._format_value_for_css({'value':1.5,'unit':'rem'},'dimension') == '1.5rem'
    parsed=tokens.parse_style_dictionary({'spacing':{'value':{'value':8,'unit':'px'},'type':'dimension'}})
    assert parsed[0].type == 'dimension'
    assert '8px' in tokens.emit_css(parsed)


def test_token_shadow_nested_dimensions():
    value={'offsetX':{'value':1,'unit':'px'},'blur':{'value':3,'unit':'px'},'color':'#000'}
    assert tokens._format_value_for_css(value,'shadow') == '1px 0 3px 0 #000'


@pytest.mark.parametrize('value,type_', [({'x':1},'typography'), ({'value':1,'unit':'em'},'dimension'), (float('nan'),'number'), (None,'color'), (True,'number'), ([1,2],'gradient')])
def test_tokens_reject_invalid_css_instead_of_silent_json(value,type_):
    with pytest.raises(ValueError): tokens._format_value_for_css(value,type_)


def test_token_unnamed_root_rejected():
    with pytest.raises(ValueError): tokens.parse_w3c_json({'$value':'red'})


def test_mcp_regression_and_full_repository_portability():
    assert '$comment' in portability.mcp_errors({'$comment':'bad','mcpServers':{}})[0]
    assert portability.mcp_errors({'mcpServers':{}}) == []
    assert portability.check(ROOT) == []


def test_generated_metadata_is_current():
    result=subprocess.run([sys.executable,str(ROOT/'scripts/sync-openai.py'),'--check'],capture_output=True,text=True,timeout=30)
    assert result.returncode == 0, result.stdout+result.stderr


def test_setup_read_only_without_install(tmp_path,monkeypatch):
    monkeypatch.setenv('PLUGIN_DATA',str(tmp_path/'data'))
    assert setup.main([]) == 1
    assert not (tmp_path/'data').exists()


def test_requirement_hash_tracks_nested_files(tmp_path):
    (tmp_path/'requirements.txt').write_text('-r child.txt\n')
    (tmp_path/'child.txt').write_text('one\n')
    before=setup.requirement_digest(tmp_path/'requirements.txt')
    (tmp_path/'child.txt').write_text('two\n')
    assert setup.requirement_digest(tmp_path/'requirements.txt') != before
    (tmp_path/'child.txt').write_text('-r requirements.txt\n')
    with pytest.raises(ValueError): setup.requirement_digest(tmp_path/'requirements.txt')


def test_setup_failed_install_never_leaves_success_stamp(tmp_path,monkeypatch):
    monkeypatch.setenv('PLUGIN_DATA',str(tmp_path))
    root=tmp_path/'venv'; (root/'bin').mkdir(parents=True)
    (root/'bin/python').write_text('fake'); (root/'.requirements-sha256').write_text('stale')
    (tmp_path/'python_path.txt').write_text('old')
    monkeypatch.setattr(setup.subprocess,'run',Mock(side_effect=subprocess.CalledProcessError(1,['pip'])))
    with pytest.raises(subprocess.CalledProcessError): setup.main(['--install'])
    assert not (root/'.requirements-sha256').exists()
    assert not (tmp_path/'python_path.txt').exists()


def test_robots_multiple_agents_and_comments(monkeypatch):
    robots=load('marketing/scripts/robots_parser.py')
    mock_client(monkeypatch,robots,text='User-agent: A\nUser-agent: B\nDisallow: /private # note\nUser-agent: A\nAllow: /public\n')
    result=robots.parse_robots('https://example.test')
    assert result['user_agents']['A']['disallow'] == ['/private']
    assert result['user_agents']['B']['disallow'] == ['/private']
    assert result['user_agents']['A']['allow'] == ['/public']
    assert result['user_agents']['B']['allow'] == []


def test_schema_malformed_json_and_empty_type():
    pytest.importorskip('selectolax')
    schema=load('marketing/scripts/schema_validator.py')
    parsed=schema._extract_json_ld('<script type="application/ld+json">{bad}</script>')
    assert schema._validate_schema(parsed[0])['status']=='invalid_json_ld'
    assert schema._validate_schema({'@type':[]})['status']=='unknown_type'
    assert schema._validate_schema({'@type':['Unknown', 'Product'],'name':''})['status']=='coverage_gaps'
    assert schema._validate_schema({'@type':'Product','name':'Example'})['status']=='coverage_pass'


def test_dashboard_sanitises_active_markdown(tmp_path,monkeypatch):
    pytest.importorskip('pandas'); pytest.importorskip('bleach')
    dashboard=load('marketing/skills/keyword-clustering-and-mapping/scripts/build_dashboard.py')
    monkeypatch.setattr(dashboard,'_markdown',types.SimpleNamespace(markdown=lambda *a,**k:'<h1>Title</h1><img src=x onerror=alert(1)><script>alert(1)</script><a href="javascript:alert(1)">bad</a>'))
    file=tmp_path/'report.md'; file.write_text('untrusted report')
    out=dashboard._render_markdown(str(file))
    assert '<h1>Title</h1>' in out
    assert '<script' not in out and 'onerror' not in out and 'javascript:' not in out


def test_clustering_focus_validation_without_loading_optional_models(tmp_path):
    # Isolate the pure input-validation function; this is NOT a pipeline test.
    source=(ROOT/'marketing/skills/keyword-clustering-and-mapping/scripts/run_clustering.py').read_text()
    tree=ast.parse(source); fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='_load_exclusions')
    namespace={'os':os,'json':json}
    exec(compile(ast.Module(body=[fn],type_ignores=[]),'<focus-input>','exec'),namespace)
    call=namespace['_load_exclusions']
    assert call(None)==[]
    with pytest.raises(ValueError): call(str(tmp_path/'missing'))
    file=tmp_path/'focus.json'; file.write_text('{"exclude": "not a list"}')
    with pytest.raises(ValueError): call(str(file))
    file.write_text('{"exclude": [" BOOKS "]}')
    assert call(str(file))==['books']


@pytest.mark.parametrize('period',['week','month','quarter'])
@pytest.mark.parametrize('metric',['retention','revenue','count'])
def test_cohort_queries_have_one_event_join(period,metric):
    query=cohort.build_time_cohort_query(period,metric,'public.events','user_id')
    assert query.count('JOIN cohort_base') == 1
    assert 'cohort_labeled' not in query
    assert "INTERVAL '1 month'" not in query
    assert ('SUM(amount)' in query) == (metric=='revenue')
    behaviour=cohort.build_behavior_cohort_query(period,metric,"it's quoted",'events','user_id')
    assert "it''s quoted" in behaviour
    assert ('SUM(amount)' in behaviour) == (metric=='revenue')
    assert 'non_behavior_cohort' not in behaviour


@pytest.mark.parametrize('table',['events; DROP TABLE x','x--comment','x y','../x',''])
def test_cohort_rejects_identifier_injection(table):
    with pytest.raises(ValueError): cohort.build_time_cohort_query('month','revenue',table,'user_id')


@pytest.mark.parametrize('new_version,expected', [('1.0.0',1),('0.9.0',1),('1.0.1',0),('1.00.2',1)])
def test_version_guard_compares_increasing_head_versions(tmp_path,new_version,expected):
    (tmp_path/'scripts').mkdir(); shutil.copy(ROOT/'scripts/check-version-bumps.mjs',tmp_path/'scripts')
    (tmp_path/'.claude-plugin').mkdir(); (tmp_path/'x/.claude-plugin').mkdir(parents=True)
    (tmp_path/'.claude-plugin/marketplace.json').write_text('{"name":"test","plugins":[{"name":"x","source":"./x"}]}')
    manifest=tmp_path/'x/.claude-plugin/plugin.json'; manifest.write_text('{"name":"x","version":"1.0.0"}')
    def git(*args):
        return subprocess.check_output(['git',*args],cwd=tmp_path,text=True,stderr=subprocess.DEVNULL).strip()
    git('init','-q'); git('config','user.name','Test'); git('config','user.email','test@example.invalid'); git('add','.'); git('commit','-qm','base'); base=git('rev-parse','HEAD')
    manifest.write_text(json.dumps({'name':'x','version':new_version})); (tmp_path/'x/change.md').write_text('changed')
    git('add','.'); git('commit','-qm','head'); head=git('rev-parse','HEAD')
    # A corrupt working tree catalogue must not affect the head-ref check.
    (tmp_path/'.claude-plugin/marketplace.json').write_text('invalid working tree')
    result=subprocess.run(['node','scripts/check-version-bumps.mjs',base,head],cwd=tmp_path,capture_output=True,text=True,timeout=20)
    assert result.returncode == expected, result.stdout+result.stderr
