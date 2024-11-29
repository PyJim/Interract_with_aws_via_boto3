import os
import boto3
from botocore.exceptions import ClientError

# Create a session
session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
    region_name=os.getenv('REGION')
)

s3 = boto3.client('s3')


# create an s3 bucket
BUCKET_NAME = 'test-user-todo-app-bucket'


def create_bucket(bucket_name):
    """create an s3 bucket

    Args:
        bucket_name (_type_): globally unique name of the bucket
    """
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
    except ClientError as e:
        # If the error is "Not Found", the bucket does not exist
        if e.response['Error']['Code'] == '404':
            try:
                # Create the bucket
                s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={
                        'LocationConstraint': 'eu-north-1'
                    }
                )
                print(f"Bucket '{bucket_name}' created successfully.")
            except boto3.exceptions.S3UploadFailedError as create_error:
                print(f"Error creating the bucket: {create_error}")
        else:
            print(f"Unexpected error: {e}")


# list buckets
def list_buckets():
    """list all s3 buckets within the region
    """
    try:
        response = s3.list_buckets()
        print("Buckets:")

        for bucket in response['Buckets']:
            print(f"  {bucket['Name']}")

    except boto3.exceptions.S3UploadFailedError as e:
        print(f"Error: {e}")


# delete bucket
def delete_bucket(bucket_name):
    """delete_bucket

    Args:
        bucket_name (_type_): name of the bucket to delete
    """
    try:
        s3.delete_bucket(
            Bucket=bucket_name
        )
        print("Bucket deleted")
    except boto3.exceptions.S3UploadFailedError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    create_bucket(BUCKET_NAME)
    list_buckets()
    delete_bucket(BUCKET_NAME)
