val = ["Even" if x%2==0 else "Odd" for x in range(1,20)]
print(val)

grades = [85, 42, 78, 50, 92]
val = ["Pass" if x >=50 else "fail" for x in grades]
print(val)