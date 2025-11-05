# Project Documentation

## Overview
Open-source Python package for workout analysis and recommendations: log ingestion, metrics, plateau detection, and progression suggestions. Professional structure, automation, tests, and robust documentation.

## Structure
- `src/trainlytics/`: Core package modules
- `notebooks/`: EDA, modeling, reporting
- `tests/`: Unit and integration tests
- `docs/`: Documentation, changelog, references
- `.github/workflows/`: CI/CD
- `data/`: Sample data

## How to Use
1. Install dependencies: `pip install -r requirements.txt`
2. Activate the virtual environment: `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\Activate.ps1` (Windows)
3. Run notebooks in `notebooks/` for full examples.
4. Run tests: `PYTHONPATH=src pytest tests` (Linux/Mac) or `$env:PYTHONPATH="$(Resolve-Path .\src)"; pytest tests` (Windows)

## Contribution
- Follow the guide in `CONTRIBUTING.md`
- Open issues and PRs
- Respect the `CODE_OF_CONDUCT.md`

## Automation
- CI/CD: Lint, test, build, and publish artifacts via GitHub Actions
- VS Code tasks: Lint, format, test

## FAIR & Reproducibility
- Versioned data and code
- Notebooks with controlled outputs
- Metadata and citation in `CITATION.cff`

## References
See `docs/references.md` for useful links and FAIR standards.
