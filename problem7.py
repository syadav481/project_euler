def isPrime(n):
    if n == 1:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def findNtPrime(n):
    prime_count = 0
    candidate = 1

    while prime_count < n:
        candidate += 1
        if isPrime(candidate):
            prime_count += 1

    return candidate


print(findNtPrime(10001))
