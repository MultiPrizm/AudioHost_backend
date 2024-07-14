import boto3, os, colorama, components.logger
from fastapi import UploadFile
from components.logger import *

class S3():

    def __init__(self, native_aunt: bool = True) -> None:
        try:
            if native_aunt:
                self.session = boto3.Session(
                    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
                    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
                    region_name=os.getenv("AWS_REGION")
                )
                self.s3 = self.session.client("s3")
            else:
                self.s3 = boto3.client("s3")
            
            print("S3[", colorama.Fore.GREEN + "OK",colorama.Style.RESET_ALL + "]: S3 connected.")
        except Exception as e:
            print("S3[", colorama.Fore.RED + "ERROR",colorama.Style.RESET_ALL + "]: S3 connect fail.")
            components.logger.error(e)
    
    def buckets_list(self):
        buckets = self.s3.list_buckets()

        return buckets["Buckets"]
    
    def upload_file(self, file: UploadFile, bucket_name: str):
        
        try:
            content = file.read()

            self.s3.upload_fileobj(
                Fileobj = content,
                Bucket = bucket_name,
                Key = file.filename
            )

            return True
        
        except Exception as e:

            return False
    
    def get_file(self, bucket: str, file: str):

        try:
            response = self.s3.get_object(Bucket=bucket, Key=file)

            return response
        except self.s3.exceptions.NoSuchKey:
            return False
        except Exception as e:
            error(e)
            return False

