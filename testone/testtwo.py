val=[x for x in range(1,11 )]
print(val)
val=[x*x for x in range(1,11)]
print(val)

val=[x*x*x for x in range(1,6)]
print(val)

val=[x*10 for x in range(1,6 )]
print(val)

val= [x for x in range(1,11) if x%2==0]
print(val)
val=[x for x in range(1,11) if x%2!=0]
print(val)

numbers = [2, 5, 7, 3, 10, 4, 15]
val=[x for x in numbers if x>5]
print(val)

numbers = [3, 5, 6, 8, 9, 12, 14, 15]
val=[x for x in numbers if x%3==0]
print(val)