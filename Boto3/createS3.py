import boto3

s3=boto3.client("s3",region_name="us-east-1")
bucket_name="amz-bkt-tst-sb-501"
s3.create_bucket(
    Bucket=bucket_name
)
print("Bucket is created",bucket_name)

