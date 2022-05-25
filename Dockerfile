FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /project_root
COPY ./project_root /project_root
WORKDIR /project_root
COPY ./scripts /scripts

RUN sed -i 's/\r$//' /scripts/entrypoint.sh && chmod +x /scripts/entrypoint.sh


RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
#Temporary solution!Give 777 permission to /project_root/dbsqlite3 so nginx can access it.
RUN chmod -R 777 /project_root
USER user

CMD ["entrypoint.sh"]
