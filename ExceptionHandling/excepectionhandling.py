
a=input("Enter a value:")
b=input("Enter b value :")
try:
    c=int(a)/int(b)
except Exception as e:
    print(f"The Exception is{e}")
else:
    print(c)
finally:
    print("Done")