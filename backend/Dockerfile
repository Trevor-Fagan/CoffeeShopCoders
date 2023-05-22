FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
CMD ["/bin/bash", "-c", "gunicorn --bind 0.0.0.0:5000 wsgi:app"]
