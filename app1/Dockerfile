# build stage
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir --progress-bar off -r requirements.txt

# runtime
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# copiamos código y assets
COPY app1.py requirements.txt ./
COPY templates ./templates/
COPY static    ./static/

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app1:app"]
