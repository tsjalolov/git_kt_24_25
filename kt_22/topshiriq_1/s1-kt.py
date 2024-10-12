def find_prime_numbers(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')

n = int(input("n ni kiriting: "))
find_prime_numbers(n)
