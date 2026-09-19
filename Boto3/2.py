import boto3

sts=boto3.client("sts")
res=sts.get_caller_identity()
print(res)
print(f"User ID is {res["UserId"]}")
print(f"Account is {res["Account"]}")
print(f"Arn is {res["Arn"]}")