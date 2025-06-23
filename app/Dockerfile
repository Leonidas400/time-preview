FROM python:3.12.1

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir requests flask pytest

EXPOSE 5000

CMD ["python3", "main.py"]
