def isPrime(n):
    if n == 1:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


ans = 0
for i in range(2000001):
    if isPrime(i):
        ans += i
print(ans)
