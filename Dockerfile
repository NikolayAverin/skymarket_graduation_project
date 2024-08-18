FROM python:3

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --upgrade pip \
    && pip install ruamel.yaml.clib\
    && pip install -r requirements.txt --no-cache-dir

COPY . .
