numbers = [3, 5, 6, 8, 9, 12, 14, 15,6,9]
va= (x for x in numbers if x%3==0)
print(list(va))

val= { x for x in numbers if x%2==0}
print(val)

nums=(1,2,3,4,5,6,7,8,9,4,5,4,3,4,5,6)
val=(i for i in nums if i%2==0)
print(list(val))


cpu_usage = [25, 80, 45, 90, 60, 30, 95]
high_cpu= (c for c in cpu_usage if c>70)
print(list(high_cpu))

num=(1,2,3,4,3,4,3)
val=[n*n for n in num]
print(val)