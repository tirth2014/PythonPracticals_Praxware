# Brute Force ( O(n^3)):
# Fails for all negative elements case

def find_maximum_subarray(arr, length):
    sumOfarr = []
    for k in range(length):
        for i in range(k, length + 1):
            s = 0
            for j in range(k, i):
                s += arr[j]
            sumOfarr.append(s)
    return (max(sumOfarr))


def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum_subarray(arr, n))


main()



#Brute Force O(n^2):

def find_maximum_subarray(arr, length):
    maxSofar = -1e8

    for i in range(length):
        maxHere = 0
        for j in range(i,length):
           maxHere = maxHere + arr[j]
           if maxHere > maxSofar:
               maxSofar = maxHere
           elif maxHere<0:
               maxHere=0
    return maxSofar
def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum_subarray(arr, n))


main()



#Kadane's algorithm O(n):

def find_maximum_subarray(arr, length):

    maxSofar = arr[0]
    maxHere = 0
    for  i in range(length):
        maxHere+=arr[i]
        if maxHere < 0:
            maxHere=0
        elif maxHere> maxSofar:
            maxSofar = maxHere

    return maxSofar

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum_subarray(arr, n))

main()

