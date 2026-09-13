import boto3
s3=boto3.client("s3")
bucket_name="amz-bkt-tst-sb-501"
try:
  respoce=s3.delete_bucket(
     Bucket=bucket_name
  )
except Exception as e:
  print("The error is",e)
else:
  print(f"{bucket_name} is deleted")
finally:
  print("Completed")
  





 
  
