FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r api/requirements.txt

EXPOSE 80

ENV FLASK_APP=api/app.py

CMD ["flask", "run", "--host=0.0.0.0"]
