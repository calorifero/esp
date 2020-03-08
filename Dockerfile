FROM python:slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
EXPOSE 3000
ENTRYPOINT [ "python", "./app.py" ]

