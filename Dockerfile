FROM python:alpine

WORKDIR /src

COPY /requirements /requirements
COPY /scripts /scripts
COPY /src .

EXPOSE "8000"

RUN pip install -r /requirements/developer.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home djad && \
    chown -R djad:djad /vol && \
    chmod -R 755 /vol


#ENV PATH="/scripts:/py/bin:$PATH"

USER djad
RUN python manage.py makemigrations && \
    python manage.py migrate

ENTRYPOINT ['python']

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
