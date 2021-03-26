import logging
import boto3
from botocore.exceptions import ClientError

class AwsService:
  def __init__(self, aws_access_key_id, aws_secret_access):
    self.access_key = aws_access_key_id
    self.secret_access = aws_secret_access

  def upload_file(self, file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
      object_name = file_name

    # Upload the file
    s3_client = boto3.client(
                    's3', 
                    aws_access_key_id=self.access_key, 
                    aws_secret_access_key=self.secret_access
                )

    try:
      response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
      logging.error(e)
      return False
    print("upload {0} to {1} ".format(file_name, bucket))
    return True
  
  def check_file(self, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
      object_name = file_name

    # Upload the file
    s3_client = boto3.client(
                    's3', 
                    aws_access_key_id=self.access_key, 
                    aws_secret_access_key=self.secret_access
                )
    
    try:
      s3_client.head_object(Bucket=bucket, Key=object_name)
    except ClientError as e:
      logging.error(e)
      return False
    return True

  def delete_file(self, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
      object_name = file_name

    # Upload the file
    s3_client = boto3.client(
                    's3', 
                    aws_access_key_id=self.access_key, 
                    aws_secret_access_key=self.secret_access
                )
    
    try:
      s3_client.head_object(Bucket=bucket, Key=object_name)
    except ClientError as e:
      logging.error(e)
      return False
    return True