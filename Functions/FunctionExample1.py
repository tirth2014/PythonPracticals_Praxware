def dataget(name,a,b):
    print("Hello Call From Function")
    print("Name is",name)
    print("Addition is:",a+b)

x=int(input("Enter no 1"))
y=int(input("Enter no 2"))
dataget("Hitesh",x,y)



def Checkvalue(a,b):
    c=a+b
    return c

print(Checkvalue(55,55))

def arbitaryfunction(*args):
    print("ID :",args[0])
    print("Name :",args[1])
    print("Emnrollemnt :",args[2])
    print("Email ID :",args[3])
    print("Mobile No :",args[4])

arbitaryfunction(1,"Hitesh",17855222555,"abc@gmail.com",9016395600)


def arbitarydouble(**kwargs):
    print("Selection : Argument",kwargs["name2"])

arbitarydouble(name1="Android",name2="Python")


def Defaultfunction1(name="hitesh",value1=0,value2=10):
    print("Name is :",name)
    print("Value 1 :",value1)
    print("Value 2",value2)

Defaultfunction1()