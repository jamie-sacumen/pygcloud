import os
#import boto3

import pytest
from pyaws.clients.s3 import S3Client


res = S3Client.instance()


json_file = 'gcloud.json'

bucket = textsmind.appspot.com"
gcloud_bucket_file_path = '/data-collector-sentinel/azure_sentinel/'
file_path = os.getcwd() + "/tests/abc.json"


def test_instance_value():
    assert res is not None


def test_positive_get_s3_client():
#sending a valid configuration  to gcloud connect
    res.connect(json_file)

    assert res._client is not None

#test case to check if non existent bucket is referred  for file transfer
def test_send_file_to_s3_bucket():
    
    bucket = "test_s3"    
    res.connect(json_file)

    assert res.send_file_to_bucket(bucket, "/data/test/", file_path,"msg")=="Error"

def test_send_file_to_valid_s3_bucket():
    res.connect(json_file)
    assert res.send_file_to_bucket(bucket, gcloud_bucket_file_path, file_path,"msg") =="Success"