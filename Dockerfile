FROM bitnami/python:latest

WORKDIR /src

COPY ./reqirements /requirements
COPY ./scripts /scripts
COPY ./src .

EXPOSE 8000

RUN /py/bin/pip install -r /requirements/developer.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home djad && \
    chown -R djad:djad /vol && \
    chmod -R 755 /vol


ENV PATH="/scripts:/py/bin:$PATH"

USER djad
CMD ["run.sh"]