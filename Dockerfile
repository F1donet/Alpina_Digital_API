FROM python:3.14-alpine

WORKDIR /Alpina_Digital_API

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["sh", "run.sh"]
