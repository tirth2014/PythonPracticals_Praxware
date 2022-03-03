def prime_numbers(n):
    primes = []
    num = 2
    count = 0
    while count < n:
        flag = 1
        for i in range(2, num):
            if num % i == 0:
                flag = 0
                break

            if flag == 1:
                primes.append(num)
                count = count + 1
            num += 1
    return primes


def main():
    n = int(input())
    output = prime_numbers(n)
    for i in range(0, n):
        print(output[i])


main()
