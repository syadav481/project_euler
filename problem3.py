def getLargestPrimeFactor(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            n /= d
            factors.append(d)
        d = d + 1
    print(max(factors))


getLargestPrimeFactor(600851475143)
