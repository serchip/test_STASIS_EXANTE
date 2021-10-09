FROM python:3.8.9-slim as runtime

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Europe/Moscow

RUN apt update -yqq \
    && apt install -yqq tzdata iputils-ping net-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# RUN mkdir /code
# RUN mkdir /code/requirements && echo
WORKDIR /code

COPY /requirements/* /code/requirements/

RUN pip install -r /code/requirements/dev.txt

ADD . /code/

EXPOSE 8000
CMD ["gunicorn", "app.buyandsell.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
