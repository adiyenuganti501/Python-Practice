servers = "web01,web02,web03,db01"
res=servers.split(",")
print(list(res))
print(res)
print(type(res))
print(res[0])
print(res[len(res)-1])
print(len(res))