# FROM python:3.10-alpine
# ENV LANG C.UTF-8
# ENV LC_ALL C.UTF-8
# WORKDIR /src

# COPY /requirements /requirements
# COPY /scripts /scripts
# COPY /src /src/

# EXPOSE 8000
# RUN pip install -r /requirements/developer.txt

# RUN chmod -R +x /scripts && \
#     mkdir -p /vol/web/static && \
#     mkdir -p /vol/web/media && \
#     adduser --disabled-password --no-create-home djad && \
#     chown -R djad:djad /vol && \
#     chmod -R 755 /vol

# ENV PATH="/scripts:/usr/lib/python3.11/site-packages/pip:$PATH"    

# CMD ["run.sh"]

# # ENV PATH="/scripts:/usr/lib/python3.11/site-packages/pip:$PATH"

# # CMD run.sh
# # ENV PATH="/scripts:/py/bin:$PATH"

# # USER djad

FROM python:3.10.2-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements /requirements
COPY /scripts /scripts
COPY /src .
RUN pip install -r requirements/developer.txt

COPY . .