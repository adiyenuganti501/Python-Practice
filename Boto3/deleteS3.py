import boto3
s3=boto3.client("s3")
bucket_name="amz-bkt-tst-sb-501"
try:
  res=s3.list_objects_v2(
    Bucket=bucket_name
  )
  if "Contents" in res:

        objects = [
            {"Key": obj["Key"]}
            for obj in res["Contents"]
  ]
        print("Ojects in Bucket found")
  s3.delete_objects(
      Bucket=bucket_name,
            Delete={
                "Objects": objects
            }
  ) 
  print("Objects in bucket got deleted")
  respoce=s3.delete_bucket(
     Bucket=bucket_name
  )
except Exception as e:
  print("The error is",e)
else:
  print(f"{bucket_name} is deleted")
finally:
  print("Completed")
  





 
  
