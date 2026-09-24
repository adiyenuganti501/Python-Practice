import boto3
sts=boto3.client("sts")    #Secure Token Service
res=sts.get_caller_identity()
#print(res)
print(res["Account"])
print(res["UserId"])
print(res["Arn"])