# StreamDB

An embedded append-only event store with time-indexed scans and deterministic compaction.

> **Status: released.** v0.9.2 is the current public release; the
> implementation is complete and the repository is public.

## Layout

```
src/         library code
configs/     default configuration
scripts/     build and release helpers
tests/       smoke tests
```

## Quick start

```bash
python -m pip install -r requirements.txt
bash scripts/run.sh --config configs/base.yaml
```

## License

MIT.
