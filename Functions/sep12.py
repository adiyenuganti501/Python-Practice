marks=(20,10,330,35,60,69,90,89)
val=filter(lambda x:x>=35, marks)
print(list(val))

print("-------------------------")
val=list(map(lambda x: x*x, range(5)))
print(val)

li=[1,2,3,4,5,6,7,8]
print(li[::-4])

li = [10, 20, 30, 40, 50, 60, 70, 80]
print(li[8:0:-2])