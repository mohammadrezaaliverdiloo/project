# FROM python:alpine
# ENV PATH="/scripts:/py/bin:$PATH"
# USER djad
# Install requirements.txt
# RUN pip install -r /app/requirements.txt
# COPY ./project/ /app
# WORKDIR /app
# RUN mkdir /app
# Install required package
###############################
FROM python:3.10-alpine
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
COPY ./project/requirements.txt /app
RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    git bash

COPY /reqirements /requirements
COPY /scripts /scripts
WORKDIR /src
COPY /src .
RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home djad && \
    chown -R djad:djad /vol && \
    chmod -R 755 /vol

EXPOSE 8000
RUN pip install -r /requirements/developer.txt
CMD ["run.sh"]