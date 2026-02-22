# base Docker image that we will build on
FROM python:3.13.11-slim

# copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /code

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
COPY pyproject.toml .python-version uv.lock ./

# Install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked

# Copy application code
COPY insert_to_pg.py .

# Set entry point
ENTRYPOINT ["uv", "run", "python", "insert_to_pg.py"]
