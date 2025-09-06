#Write a python script to create a list of first n prime numbers.
def first_n_primes(n):
    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

        num += 1
    return primes
print(first_n_primes(10))