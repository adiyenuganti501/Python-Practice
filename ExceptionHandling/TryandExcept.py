a=input("Enter a Value::")
b=input("Enter b Value::")
try:
    c=int(a)/int(b)
    print("The C Value is::",int(c))
    
except Exception as e:
    print("The Exception is::",e)
finally:
    print("This is Finally Block")