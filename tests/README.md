# Tests

Smoke tests for plugin-level Python scripts in the business marketplace.

```bash
python tests/scripts/test_smoke.py
python -m pytest tests/scripts/test_smoke.py -v
```

| Script | Test class | Cases |
|---|---|---|
| `data-science/scripts/power-calc.py` | `TestPowerCalc` | standard A/B / smaller-MDE-bigger-N |
| `economics/scripts/cvp-calc.py` | `TestCvpCalc` | basic break-even / negative-margin-errors |

Pure stdlib only — no third-party dependencies.
