def add(a, b):
    return a + b
def su(a,b):
    return a - b
def mul(a,b):
    return a * b
lst=[add, su, mul]
for l in lst:
    print(l(20,3))
