import boto3
from fastapi import UploadFile
from components.logger import *

class S3():

    s3 = boto3.client("s3")

    @staticmethod
    def buckets_list():
        buckets = S3.s3.list_buckets()

        return buckets["Buckets"]
    
    @staticmethod
    def upload_file(file: UploadFile, bucket_name: str):
        
        try:
            content = file.read()

            S3.s3.upload_fileobj(
                Fileobj = content,
                Bucket = bucket_name,
                Key = file.filename
            )

            return True
        
        except Exception as e:

            return False
    
    @staticmethod
    def get_file(bucket: str, file: str):

        try:
            response = S3.s3.get_object(Bucket=bucket, Key=file)

            return response
        except S3.s3.exceptions.NoSuchKey:
            return False
        except BaseException as e:
            error(e)

