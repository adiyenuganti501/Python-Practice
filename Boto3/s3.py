import boto3
try:
 s3=boto3.client("s3")
 val=s3.list_buckets()
 for i in val["Buckets"]:
    print("Bucket Name:", i["Name"])
    print("Date of creation:", i["CreationDate"])
except Exception as e:
 print(e)

finally:
  print("Done")