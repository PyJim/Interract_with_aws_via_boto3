# AWS S3 Interaction with Python and Boto3

This lab demonstrates how to interact with AWS resources using a Python application and the **Boto3** library. The primary focus is creating, listing, and deleting an Amazon S3 bucket programmatically.

## Prerequisites

Before running the script, ensure the following:

1. **AWS Account**: You must have an AWS account.
2. **AWS IAM User**: The IAM user should have the necessary permissions for S3 (e.g., `AmazonS3FullAccess` or equivalent custom policy).
3. **Python Installed**: Install Python (3.6 or later).
4. **Boto3 Installed**: Install Boto3 by running:
   ```bash
   pip install boto3
   ```
5. **Environment Variables**: Set the following environment variables in your system:
   - `ACCESS_KEY_ID`: Your AWS access key ID.
   - `SECRET_ACCESS_KEY`: Your AWS secret access key.
   - `REGION`: Your preferred AWS region (e.g., `eu-north-1`).

## Features

The script performs the following actions:

1. **Checks if a Bucket Exists**:
   - If the bucket already exists, it prints a message.
   - If not, it attempts to create the bucket.

2. **Creates a New S3 Bucket**:
   - Creates a bucket with a specified name and region.

3. **Lists All Buckets**:
   - Lists all buckets in the AWS account.

4. **Deletes the Bucket**:
   - Deletes the bucket created during the lab.

## How to Run the Script

1. Clone or copy the repository/files to your local machine.
2. Navigate to the directory containing the script.
3. Ensure the required environment variables are set. Example for Linux/macOS:
   ```bash
   export ACCESS_KEY_ID=<your-access-key-id>
   export SECRET_ACCESS_KEY=<your-secret-access-key>
   export REGION=eu-north-1
   ```
   For Windows (Command Prompt):
   ```cmd
   set ACCESS_KEY_ID=<your-access-key-id>
   set SECRET_ACCESS_KEY=<your-secret-access-key>
   set REGION=eu-north-1
   ```
4. Run the script:
   ```bash
   python <script_name>.py
   ```

## Expected Output

The script will produce output similar to the following, depending on whether the bucket already exists, is created successfully, or is deleted:

```
Bucket 'test-user-todo-app-bucket' already exists.
Buckets:
  test-user-todo-app-bucket
  another-example-bucket
Bucket deleted
```

## Common Errors

- **`ClientError: Access Denied`**:
  - Ensure the IAM user has the appropriate S3 permissions.
- **`ClientError: InvalidAccessKeyId`**:
  - Verify the AWS credentials are correct.
- **`S3UploadFailedError`**:
  - Ensure the specified bucket name and region comply with AWS naming rules and region constraints.

## Notes

- Bucket names must be globally unique across all AWS accounts.
- To avoid accidental data loss, ensure the bucket is empty before attempting deletion.
- Modify the `BUCKET_NAME` variable in the script to test with different bucket names.
