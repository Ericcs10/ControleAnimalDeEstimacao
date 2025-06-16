# Etapa de build
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt .

RUN pip install --user --no-warn-script-location -r requirements.txt

# Etapa final
FROM python:3.12-slim-bookworm

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY ./app ./app 

ENV PATH=/root/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
