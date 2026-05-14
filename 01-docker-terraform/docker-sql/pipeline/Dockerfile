FROM python:3.13.11-slim
# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# working directory
WORKDIR /code
# Add virtual environment to PATH so we can use installed packages
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

# running under the currently directory
COPY pipeline.py .

# when you run the docker it would run this
ENTRYPOINT ["python", "pipeline.py"]