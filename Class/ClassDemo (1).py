xyz=10
class Myclass:
    name="hitesh"
    n1=10
    n2=20
    xyz=10
    def adddata(self,no1,no2,name):
        print(no1+no2)
        print("Name :",name)

class Myclass1(Myclass):

    def showall(self):
        print(Myclass.name)
        print(Myclass.n1+Myclass.n2)

    def savedata(self,salay,ta,da,hra,pf):
        print(Myclass.name)
        print(Myclass.n1+Myclass.n2)
    def readata(self,salay,ta,da,hra,pf):
        print(Myclass.name)
        print(Myclass.n1+Myclass.n2)



a=int(input("Enter No 1"))
b=int(input("Enter No 2"))
name1=input("Enter Name")

obj=Myclass1()
obj.adddata(a,b,name1)
obj.showall()