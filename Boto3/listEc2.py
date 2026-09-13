import boto3

s3=boto3.client("s3")

response = s3.list_buckets()
# print(response.keys())
# print(response["Buckets"])

for bucket in response["Buckets"]:
  print("Buckets Name:", bucket["Name"])

# for bucket in response["Buckets"]:
#     print("Bucket Name:", bucket["Name"])