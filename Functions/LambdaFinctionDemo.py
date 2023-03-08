double=lambda x:x*2
print(double(10))

list1=[10,1,2,5,4,8,9]

newlist=list(filter(lambda x:(x%2==0),list1))

print(newlist)

datalist=[1,3,5,7,8,9,10,11]
newlist=list(map(lambda x:x*2,datalist))

print(newlist)