# syntax=docker/dockerfile:1

FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1         PYTHONUNBUFFERED=1         PIP_NO_CACHE_DIR=1

# System deps (add build tools if you need to compile wheels)
RUN apt-get update && apt-get install -y --no-install-recommends         curl ca-certificates tini &&         rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Separate layer for deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN useradd -u 10001 -m appuser
USER appuser

# Copy app
COPY --chown=appuser:appuser app/ app/

# Expose and default port
ENV PORT=8080
EXPOSE 8080

# Use tini as PID 1 for proper signal handling
ENTRYPOINT ["/usr/bin/tini", "--"]

# Start uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
