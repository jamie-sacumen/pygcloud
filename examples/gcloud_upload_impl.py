
 
from pyaws.clients.s3 import S3Client


if __name__ == "__main__":
    s3 = S3Client.instance()
    s3.connect('gcloud.json')
    s3.send_file_to_bucket("default-bucket", "/data-collector/o365/", "test.txt")
