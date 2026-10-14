# trainlytics

[![PyPI version](https://img.shields.io/pypi/v/trainlytics.svg)](https://pypi.org/project/trainlytics/)
![status](https://img.shields.io/badge/status-early%20prototype-lightgrey)

> **Early prototype (v0.1.0).** This was my first attempt at a published Python package for training data — small on purpose, and kept here as a record of where things started. The ideas grew into [Workout Insights & Planner](https://github.com/Raoc1987/Workout-Insights-Planner) and, later, into [ALKMIA](https://raoc1987.github.io/#alkmia).

## What it actually does

Five small functions, built on pandas:

| Module | Function | What it does |
|---|---|---|
| `ingest` | `load_workout_log(path)` | Reads a workout CSV |
| `clean` | `clean_workout_data(df)` | Drops empty rows, normalizes column names |
| `features` | `compute_volume(df)` | Total volume (sets × reps × weight) per exercise |
| `model` | `detect_plateau(df)` | Flags a plateau when the last 3 volume values vary less than 10% |
| `recommender` | `suggest_progression(df)` | Suggests +5% load per exercise |

Expected CSV columns: `date, exercise, sets, reps, weight`.

## Install

```bash
pip install trainlytics
```

```python
from trainlytics.ingest import load_workout_log
from trainlytics.clean import clean_workout_data
from trainlytics.features import compute_volume

df = clean_workout_data(load_workout_log("data/sample_workout_log.csv"))
print(compute_volume(df))
```

## Known limits

- The plateau rule looks at the last 3 rows, not at weekly aggregates.
- The progression rule is a flat +5%, with no fatigue or deload logic.
- Not maintained. For a more complete version, see Workout Insights & Planner.

## License

MIT
