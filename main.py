# rotate array by d elements
"""
def rot(d,n,ar=[]):
    emp=[]
    for i in range(d):
        emp.append(ar[i])
    for i in range(d-1):
        del ar[i]
    for i in range(d):
        for j in range(n-3):
            ar[j] = ar[j+1]
        ar.append(emp[i])
    print(emp)
    print(ar)
ar = [1,2,3,4]
rot(2,4,ar)

"""


# MaxPairwiseProduct

def maxPairwiseProd(n, arr=[]):
    maxProd = 0
    for i in range(0, n - 1):
        for j in range(1, n):
            prod = arr[i] * arr[j]
            if (prod > maxProd):
                maxProd = prod

    return (maxProd)


num = int(input())
"""lst= []
for i in range(num):
    a = int(input())
    lst.append(a)"""
lst = [int(i) for i in input().split()][:num]  # to take n space separated Integer in a list in python
print(maxPairwiseProd(num, lst))
