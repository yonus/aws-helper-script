import boto3;
import contextlib;
import requests;
from io import BytesIO;

s3 = boto3.resource('s3');
s3Client = boto3.client('s3')
for bucket in s3.buckets.all():
  print(bucket.name)


url = "@resource url";
with contextlib.closing(requests.get(url, stream=True, verify=False)) as response:
        # Set up file stream from response content.
        fp = BytesIO(response.content)
        # Upload data to S3
        s3Client.upload_fileobj(fp, 'aws-books', 'reviews_Electronics_5.json.gz')

