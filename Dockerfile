FROM python:3.9

ENV PYTHONUNBUFFERED 1

ENV ENV API_SECRET_KEY="django-insecure-zv-czil2aib8@ex@n+k#nh62r-p3r4t3dufvc4at=w"

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app