emp = open("Employee Salary Slip File.txt", "w")

name = input("enter name: ")
empId = int(input('enter emp id: '))
pos = input("enter position in company: ")
mob = int(input("enter mobile no.: "))
email = input("enter email id: ")
address = input("enter address: ")
salary = int(input("enter your salary: "))
TA = salary * int(input("enter TA: ")) / 100
DA = salary * int(input("enter DA: ")) / 100
HRA = salary * int(input("enter HRA: ")) / 100
PF = salary * int(input("enter PF: ")) / 100

net = TA + DA + HRA - PF
totalSal = net + salary

emp.write("EMPLOYEE DETAILS".center(50))
emp.write("\n***************************************")
emp.write("\nEmployee Name:          "f"{name} ")
emp.write("\nEmployee ID:            "f"{id} ")
emp.write("\nEmployee Position:      "f"{pos} ")
emp.write("\nEmployee Mobile Number: "f"{mob} ")
emp.write("\nEmployee Email ID:      "f"{email} ")
emp.write("\nEmployee Address:       "f"{address} ")
emp.write("\nEmployee Salary:        "f"{salary} ")
emp.write("\nTA:                     "f"{TA} ")
emp.write("\nDA:                     "f"{DA} ")
emp.write("\nHRA:                    "f"{HRA} ")
emp.write("\nPF:                     "f"{PF} ")
emp.write("\nSalary:                 "f"{salary} ")
emp.write("\nTotal Salary:           "f"{totalSal} ")
emp.write("\n***************************************")

emp.close()
print("values are added!")
