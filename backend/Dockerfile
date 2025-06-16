# Etapa 1 - Instala dependências
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt .
RUN pip install --user --no-warn-script-location -r requirements.txt

# Etapa 2 - Imagem final
FROM python:3.12-slim-bookworm

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY ./app ./app
COPY ./tests ./tests
COPY requirements.txt .

ENV PATH=/root/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
