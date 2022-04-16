FROM python:3.9-buster

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONPATH=/app/package
ENV LAMBDA_ZIP_ARCHIVE=/data/my-deployment-package.zip

# see https://notify-bot.line.me/doc/ja/
ENV LINE_TOKEN **YOUR_LINE_TOKEN**
# see  https://developers.line.biz/ja/docs/messaging-api/sticker-list/
ENV LINE_STICKER_PACKAGE_ID 6325
ENV LINE_STICKER_ID 10979923

COPY app /app
WORKDIR /app
ADD https://gist.githubusercontent.com/holly/49a5f065026e487ec803b8e2b4fb9d81/raw/lambda_function_for_aws_console_login.py lambda_function.py
RUN apt update \
 && apt install -y zip unzip \
 && apt clean \
 && rm -frv /var/lib/apt/lists/* \
 && mkdir package \
 && pip install -t ./package requests git+https://github.com/holly/pyline_notify.git \
 && chmod +x lambda_function.py
CMD [ "./make_lambda_zip.sh" ]
