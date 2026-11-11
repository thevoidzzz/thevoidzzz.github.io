# Waiting

A static page. It is not another product. It does not call an API, and it does not create a codespace.

The page repeats numbers a command already printed, including the misses, and the local order for trying the four repositories.

## Tests

GitHub Actions runs `pytest` on pull requests and on pushes to `main`. The job installs no model client and uses no API key.

```bash
pip install pytest
pytest
```

## Changes

Open a pull request against `main`. The `test` check has to pass before merge.

Architecture and decisions live in `docs/architecture/` and `docs/adr/`.
