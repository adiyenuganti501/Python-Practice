marks=(20,10,330,35,60,69,90,89)
val=filter(lambda x:x>=35, marks)
print(list(val))

print("-------------------------")
val=list(map(lambda x: x*x, range(5)))
print(val)