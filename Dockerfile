FROM python:3.12-slim

WORKDIR /app

COPY application/ ./application/

CMD ["python", "application/app.py"]