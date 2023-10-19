def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def largestPalindromeProduct():
    ans = -1
    for i in range(100, 1000):
        for j in range(100, 1000):
            curr = i * j
            if isPalindrome(curr):
                ans = max(curr, ans)
    print(ans)


largestPalindromeProduct()
