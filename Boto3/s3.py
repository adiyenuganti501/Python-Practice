import boto3
s3=boto3.client("s3")
val=s3.list_buckets()
# print(val.keys())
# print(val["Buckets"])

for i in val["Buckets"]:
    print("Bucket Name:", i["Name"])
    print("Date of creation:", i["CreationDate"])