numbers = [3, 5, 6, 8, 9, 12, 14, 15]
val=[x for x in numbers if x%3==0]
print(val)

names = ["adi", "ravi", "kiran", "raj"]

val=[x.upper() for x in names]
print(val)

words = ["apple", "banana", "avocado", "mango", "amazon"]
val=[x for x in words if x.startswith("a")]
print(val)

words = ["apple", "banana", "avocado", "mango", "amazon"]
val=[len(x) for x in words ]
print(val)


numbers = [1, 2, 3, 4, 5, 6]
result = ["even" if x%2 ==0 else "odd" for x in numbers]
print(result)





numbers = [1, 2, 3, 4, 5, 6]
res=["even" if x%2==0  else "odd" for x in numbers  ]
print(res)



marks = [35, 80, 45, 20, 90, 55]

ress= ["pass" if mark>= 35 else "fail" for mark in marks]
print(ress)


marks = [35, 80, 45, 20, 90, 55]
val=["Pass" if ma>= 35 else "Fail" for ma in marks]
print(val)