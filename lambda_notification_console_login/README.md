# lambda_notification_console_login

When AWS Console login, login alert be notified of your LINE Account.

## versions

* Python 3.9

## reference

* [LINE Notify API Document](https://notify-bot.line.me/doc/ja/)
* [送信可能なスタンプリスト](https://developers.line.biz/ja/docs/messaging-api/sticker-list/)
* [.zip ファイルアーカイブで Python Lambda 関数をデプロイする](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/python-package.html)

## build

### prerequirement

* edit Dockerfile's LINE_TOKEN
* (Optional) Dockerfile's LINE_STICKER_PACKAGE_ID and LINE_STICKER_ID
* save zip archive directory(sample dirname: /data/lambda_notification_console_login)

### execute build.sh

```
./build.sh
docker run --rm -it --mount type=bind,src=/data/lambda_notification_console_login,dst=/data -it holly/lambda_notification_console_login
```

/data/lambda_notification_console_login/my-deployment-package.zip is generated.
