# Sample Python Service (FastAPI)

A minimal service for DevOps CI/CD exercises. Exposes `/healthz`, `/readyz`, `/version`, `/sum`, and `/items/{id}`.

## Quickstart (local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make run     # or: uvicorn app.main:app --host 0.0.0.0 --port 8080
```

Open http://localhost:8080/docs

## Tests
```bash
make test
```

## Docker
```bash
docker build -t sample-python-service:dev .
docker run --rm -p 8080:8080 sample-python-service:dev # then curl http://localhost:8080/healthz
```

## Notes
- App listens on **8080** by default to align with Kubernetes `targetPort`.
- Dockerfile runs as **non-root** (UID 10001) and uses `tini` for clean shutdowns.
