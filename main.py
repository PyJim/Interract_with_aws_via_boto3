import os
import boto3
from botocore.exceptions import ClientError

# Create a session (optional if you want to use specific credentials or region)
session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
    region_name=os.getenv('REGION')
)

s3 = boto3.client('s3')


# create an s3 bucket
BUCKET_NAME = 'test-user-todo-app-bucket'


try:
    s3.head_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket '{BUCKET_NAME}' already exists.")
except ClientError as e:
    # If the error is "Not Found", the bucket does not exist
    if e.response['Error']['Code'] == '404':
        try:
            # Create the bucket
            response = s3.create_bucket(
                Bucket=BUCKET_NAME,
                CreateBucketConfiguration={
                    'LocationConstraint': 'eu-north-1'  # Specify the region
                }
            )
            print(f"Bucket '{BUCKET_NAME}' created successfully.")
        except boto3.exceptions.S3UploadFailedError as create_error:
            print(f"Error creating the bucket: {create_error}")
    else:
        print(f"Unexpected error: {e}")


# list buckets
try:
    response = s3.list_buckets()
    print("Buckets:")

    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")

except boto3.exceptions.S3UploadFailedError as e:
    print(f"Error: {e}")


# delete bucket
try:
    s3 = boto3.client('s3')
    response = s3.delete_bucket(
        Bucket=BUCKET_NAME
    )
    print("Bucket deleted")
except boto3.exceptions.S3UploadFailedError as e:
    print(f"Error: {e}")
