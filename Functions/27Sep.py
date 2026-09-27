from functools import reduce

val = filter(lambda x: x%2!=0, range(1,20))
print(list(val))

val = map(lambda x: x*x, range(1,6))
print(list(val))

val = reduce(lambda x,y: x+y, range(1,11))
print(val)