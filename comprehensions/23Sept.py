val=[x for x in range(1,10)]
print(val)

val=[x for x in range(1,10) if x%2==0]
print(val)

val=["Even" if x%2==0 else "Odd" for x in range(1,10)]
print(val)


val={x:x*x for x in range(1,5)}
print(val)