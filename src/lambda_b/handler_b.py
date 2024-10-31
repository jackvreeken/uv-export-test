import logging
import os
from logging import getLogger

import boto3
import boto3.s3.transfer as s3transfer


logging.basicConfig()
log = getLogger()
log.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

cloudwatch = boto3.client("cloudwatch")


def handler(event, context):
    log.debug(f"Incoming event:\n{event}")
    s3transfer.TransferConfig(use_threads=True, max_concurrency=20)
