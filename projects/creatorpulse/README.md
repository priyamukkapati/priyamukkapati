# CreatorPulse

A small prototype for creator recommendations and notification events.

## Current implementation

Scores creators by overlapping interest tags, excludes followed creators, returns Top-K results with stable ID-based tie breaking, and deduplicates notification events.

## Run

From the repository root, with Python 3.10+:

```bash
python3 projects/creatorpulse/app.py
```

The demo ranks code-with-sam before data-with-jo for the interests python and backend.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Limitations

This is a rule-based ranker, not a trained ML model. The outbox is in memory and does not deliver notifications or persist events.

## Roadmap

Add a FastAPI API, persist activity and outbox events in PostgreSQL, evaluate ranking quality on a real dataset, and add background delivery workers.
