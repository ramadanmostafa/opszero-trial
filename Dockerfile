FROM python:3.9-slim-buster

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libsasl2-dev python3-dev libpq-dev gcc \
    && apt-get -y clean


RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" >>  /etc/apt/sources.list.d/pgdg.list
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN apt-get install -y wget ca-certificates
RUN apt-get install -y postgresql-client


# default env variables for dev env
ENV DB_PRIMARY_HOST "db1.host.rds"
ENV DB_PRIMARY_PORT "5432"
ENV DB_PRIMARY_USERNAME "postgres"
ENV DB_PRIMARY_PASSWORD "postgres"
ENV DB_PRIMARY_NAME "canal_prod"

ENV DB_SECONDARY_HOST "db2.host.rds"
ENV DB_SECONDARY_PORT "5432"
ENV DB_SECONDARY_USERNAME "postgres"
ENV DB_SECONDARY_PASSWORD "postgres"

COPY sync_db.py /usr/src/app
COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "sync_db.py"]