FROM python:3.11-slim

WORKDIR /code

RUN apt-get update && apt-get install -y gcc

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY .env.docker /code/.env.docker

COPY . /code

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
