#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3
import json
import csv
import uuid
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TMP_PATH = "/tmp"

s3_client = boto3.client('s3')
dynamodb_client = boto3.resource('dynamodb')


def get_file_from_s3(bucket, item):
    file_name = str(uuid.uuid4())
    s3_client.download_file(bucket, item, os.path.join(TMP_PATH, file_name))
    return file_name


def save_to_db(data):
    table = dynamodb_client.Table("case")
    response = table.put_item(
        Item={
            "csv_data": data
        }
    )
    return response


def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    item = event["Records"][0]["s3"]["object"]["key"]
    logger.info(f"Item getting from {bucket}. Item: {item}")

    file_name = get_file_from_s3(bucket, item)
    logger.info(f"Item downloaded. File: {file_name}")

    results = list()

    with open(os.path.join(TMP_PATH, file_name), "r") as csv_file:
        csv_as_dict = csv.DictReader(csv_file)
        logger.info(f"CSV loaded as a dict. Content: {csv_as_dict}")

        for row in csv_as_dict:
            results.append(save_to_db(json.dumps(row)))
            logger.info(f"Line imported to the db. Line: {row}")

    return results
