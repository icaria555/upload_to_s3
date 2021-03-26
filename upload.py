from aws_service import AwsService
from os import listdir
from os.path import isfile, join
from dotenv import load_dotenv
import os

load_dotenv()

path = "output/"
path_files = [path + f for f in listdir(path) if isfile(join(path, f))]
path_files.sort()

aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY_ID')
bucket = os.getenv('AWS_BUCKET_NAME')

aws = AwsService(aws_access_key, aws_secret_key)

for p in path_files:
  aws.upload_file(p, bucket)