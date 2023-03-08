
try:
    a=int(input("Enter no 1"))
    b=int(input("Enter no 2"))
except Exception as e:
    print(e)
else:
    print("Sum",a+b)
