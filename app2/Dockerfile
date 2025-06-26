# Etapa de build
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir --progress-bar off -r requirements.txt

# Etapa runtime
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copiamos el código y las carpetas tal cual
COPY app2.py requirements.txt ./
COPY templates ./templates/
COPY static ./static/

EXPOSE 8181
# Usamos gunicorn como WSGI para evitar errores de threading
CMD ["gunicorn", "-b", "0.0.0.0:8181", "app2:app"]
