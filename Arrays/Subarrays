def print_subarray(arr, length):
    for k in range(length):
        for i in range(k, length + 1):
            for j in range(k, i):
                print('{}'.format(arr[j]), end='')
            if i<length and i>0:
                print()


def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print_subarray(arr, n)


main()
