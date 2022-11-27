FROM python:3.9-slim

ENV PORT=8000

WORKDIR /app

COPY ./app .

COPY requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN python training.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
