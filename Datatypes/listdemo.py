thislist=["A","b","c","d"]

"""print(thislist)

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

"""

#range index
print(thislist[2:5])

#begin
print(thislist[:4])

#end
print(thislist[2:])

thislist[1]="BOX"

print(thislist)


if "c" in thislist:
    print("Yes available")
else:
    print("Not Availbel")

thislist.append("e")
print(thislist)

thislist.insert(1,"a")
print(thislist)

thislist.remove("BOX")
print(thislist)

#del thislist
print(thislist)
thislist.clear()
print(thislist)

list1=["A","B","C"]
list2=["a","b","c"]

list3=list1+list2
print(list3)

list1.extend(list2)
print(list1)








