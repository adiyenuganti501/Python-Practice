try:
    a=input("Enter a value::")
    b=input("Enter b value::")
    c=int(a)/int(b)
except Exception as e:
    print(f"The error is {e}")
else:
    print(c)
finally:
    print("the execution is completed")