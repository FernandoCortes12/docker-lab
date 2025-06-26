# build
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir --progress-bar off -r requirements.txt

# runtime
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# copiamos todo
COPY app3.py index.html ./

EXPOSE 8888
CMD ["gunicorn", "-b", "0.0.0.0:8888", "app3:app"]
