FROM python:3.10.8-alpine3.15

WORKDIR /app

COPY . .

CMD [ "python", "main.py" ]