FROM python:3.8-alpine
WORKDIR /usr/src/app
COPY . .
ENTRYPOINT ["python", "fibonacci.py"]
