from functools import reduce

num=[1,2,3,4,5,6,7,8]
val=list(filter(lambda x:x%2==0,num))
print(val)

num=[1,2,3,4,5,6,7,8]
val=list(map(lambda x: x*x, num))
print(val)

num=[1,2,3,4,3,3,2,4,3]
val=[reduce(lambda x,y: x*y,num)]
print(val)

val=list(map(lambda x:x*x, range(5)))
print(val)