FROM python:3.10-alpine
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
WORKDIR /src

COPY /requirements /requirements
COPY /scripts /scripts
COPY /src .

EXPOSE 8000
RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    git bash

RUN pip install -r /requirements/developer.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home djad && \
    chown -R djad:djad /vol && \
    chmod -R 755 /vol
ENV PATH="/scripts/usr/local/lib/python3.10/site-packages:$PATH"

CMD ["run.sh"]
# ENV PATH="/scripts:/py/bin:$PATH"

# USER djad