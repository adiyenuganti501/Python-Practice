import boto3

sts = boto3.client("sts")

response = sts.get_caller_identity()

# # print(response)
print(f"User Id:{response["UserId"]}")
print("Account:", response["Account"])
print("ARN:", response["Arn"])

