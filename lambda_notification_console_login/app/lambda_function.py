#!/usr/bin/env python
# vim:fileencoding=utf-8

""" [NAME] script or package easy description

[DESCRIPTION] script or package description
"""
import os, sys, io
import json
from pyline_notify import PyLINENotify

__author__  = 'holly'
__version__ = '1.0'

DESCRIPTION = 'this is description'
MESSAGE = """
{eventTime}: AWS Console login notification
---
eventID:   {eventID}
eventName: {eventName}
arn:       {arn}
remote IP: {sourceIPAddress}
"""


def lambda_handler(event, context):

    line = PyLINENotify(os.environ["LINE_TOKEN"])
    message = MESSAGE.format(eventTime=event["detail"]["eventTime"], eventID=event["detail"]["eventID"], eventName=event["detail"]["eventName"], arn=event["detail"]["userIdentity"]["arn"], sourceIPAddress=event["detail"]["sourceIPAddress"])

    # see https://developers.line.biz/ja/docs/messaging-api/sticker-list/
    kwargs = {}
    if os.environ.get("LINE_STICKER_PACKAGE_ID"):
        kwargs["stickerPackageId"] = os.environ.get("LINE_STICKER_PACKAGE_ID")
    if os.environ.get("LINE_STICKER_ID"):
        kwargs["stickerId"] = os.environ.get("LINE_STICKER_ID")
    res = line.notify(message, **kwargs)
    print("=========================")
    print(res.status_line())
    print("=========================")
    return { "message": res.status_line() }

if __name__ == '__main__':
    event = json.load(open("event.json", "r"))
    context = {}
    res = lambda_handler(event, context)
    print(res)
