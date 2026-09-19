"""Execute generated SQL only on the explicit ephemeral regression database."""
import os
import importlib.util
from pathlib import Path
import pytest
DSN=os.environ.get('TEST_POSTGRES_DSN')
pytestmark=pytest.mark.skipif(not DSN,reason='No explicit ephemeral PostgreSQL test DSN')

@pytest.mark.parametrize('period,expected_offsets',[('month',[0,1,2,3]),('quarter',[0,1]),('week',[0,4,8,9])])
def test_calendar_periods_and_no_revenue_multiplication(period,expected_offsets):
    psycopg=pytest.importorskip('psycopg')
    path=Path(__file__).resolve().parents[1]/'data-science/skills/cohort-analysis-builder/scripts/cohort-query-builder.py'
    spec=importlib.util.spec_from_file_location('cohort_sql',path); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    # TEMP table is session-local; rollback on close. No existing table is touched.
    with psycopg.connect(DSN) as connection:
        with connection.cursor() as c:
            c.execute("SET TIME ZONE 'UTC'")
            c.execute('CREATE TEMP TABLE events(user_id text, created_at timestamptz, event_type text, amount numeric)')
            c.executemany('INSERT INTO events VALUES(%s,%s,%s,%s)',[
                ('u','2024-01-31','signup',10),('u','2024-01-31','purchase',20),
                ('u','2024-02-29','purchase',30),('u','2024-03-31','purchase',40),('u','2024-04-01','purchase',50)])
            c.execute(module.build_time_cohort_query(period,'revenue','events','user_id')); rows=c.fetchall()
            assert sum(r[2] for r in rows)==150
            assert [r[1] for r in rows]==expected_offsets
            c.execute(module.build_behavior_cohort_query(period,'revenue','signup','events','user_id'))
            assert sum(r[2] for r in c.fetchall())==150
            c.execute(module.build_time_cohort_query(period,'retention','events','user_id'))
            assert all(r[2]==1 for r in c.fetchall())
