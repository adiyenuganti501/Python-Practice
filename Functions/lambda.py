from functools import reduce
l=[1,2,3,4,5]
new_list=[]
for i in l:
    new_list.append(i*5)
print(new_list)

val=map(lambda x:x*5,l)
print(list(val))

val=filter(lambda x:x%2==0,l)
print(list(val))

val=reduce(lambda x,y:x+y,l)
print(val)
print("-----------------------------")

aa=lambda x:x*x
print(aa(5))

bb= lambda x,y:x+y
print(bb(5,6))