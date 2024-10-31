import logging
import os

import boto3
import urllib3

logging.basicConfig()
log = logging.getLogger()
log.setLevel(os.environ.get("LOG_LEVEL", "INFO"))


def handler(event, context) -> None:
    boto3.client("ssm")
    urllib3.PoolManager()
