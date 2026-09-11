try:
    a= input("Enter a Value: ")
    b= input("Enter b value: ")
    c= int(a)/int(b)
except Exception as e:
    print("The Error is :",e)
else:
    print("The Result is :",c)
finally:
    print("The Program is Completed")