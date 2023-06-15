import boto3
from dotenv import load_dotenv
from botocore.client import Config
import os


def put_object(trm, fch, dir_tramite, arch):
    load_dotenv()
    # print(f"{trm}/{fch}/{trm}/{dir_tramite.name}/{arch}")

    with open(f"{dir_tramite}/{arch}", 'rb') as f:
        data = f.read()

    s3_client = boto3.resource(
        's3',
        aws_access_key_id=os.environ.get('ENV_AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('ENV_AWS_SECRET_ACCESS_KEY'),
        region_name=os.environ.get('ENV_AWS_REGION_NAME')
    )

    s3_client.Bucket(os.environ.get('ENV_AWS_S3_BUCKET_NAME')) \
        .put_object(Key=f"{trm}/{fch}/{trm}/{dir_tramite.name}/{arch}", Body=data)

    f.close()
