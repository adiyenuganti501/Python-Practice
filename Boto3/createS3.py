import boto3

s3=boto3.client("s3",region_name="us-east-1")
bucket_name="amz-bkt-tst-sb-501"
s3.create_bucket(
    Bucket=bucket_name
)
print("Bucket is created",bucket_name)

s3.upload_file(
    Filename="Boto3/test.txt",
    Bucket=bucket_name,
    Key="test.txt" 
)
print("File uploaded successfully")

