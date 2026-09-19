numbers = [3, 5, 6, 8, 9, 12, 14, 15,6,9]

res= [x for x in numbers if x%3==0]
print(res)

cpu_usage = [25, 80, 45, 90, 60, 30, 95]
res=[i for i in cpu_usage if i>=75]
print("The CPU more than 75% is::" , res)

cpu_usage = [25, 80, 45, 90, 60, 30, 95]
res=filter(lambda x: x>=75,cpu_usage)
print(list(res))