import boto3
from dotenv import load_dotenv
import os


def get_object(arch):
    load_dotenv()
    # print(f"{trm}/{fch}/{trm}/{dir_tramite.name}/{arch}")

    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('ENV_AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('ENV_AWS_SECRET_ACCESS_KEY'),
        region_name=os.environ.get('ENV_AWS_REGION_NAME')
    )
    s3_client.download_file(
        Bucket=os.environ.get('ENV_AWS_S3_BUCKET_NAME'),
        Key=(str(arch).replace('\\', '/')),
        Filename=arch.name)
