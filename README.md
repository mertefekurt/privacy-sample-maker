<img src="assets/readme-cover.svg" alt="Privacy Sample Maker cover" width="100%" />

# Privacy Sample Maker

Create deterministic privacy-safe CSV samples from schemas.

![stack](https://img.shields.io/badge/stack-Python-dc2626?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-7c3aed?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-0891b2?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-b45309?style=flat-square)

| Question | Answer |
| --- | --- |
| What is it? | A focused Python utility for privacy review. |
| How does it run? | `privacy-sample-maker` |
| Why keep it small? | Easier review, easier tests, fewer moving parts. |

## Command

```bash
python -m pip install -e ".[dev]"
privacy-sample-maker examples/schema.csv
```

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m privacy_sample_maker --help
```
