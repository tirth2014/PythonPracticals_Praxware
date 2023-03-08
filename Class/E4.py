try:
    a = int(input("Enter no 1"))
    b = int(input("Enter no 2"))
    print(a/b)
except Exception as e:
    print(e)
finally:
    print("Finally Called")
