def checkDivisibility(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    return True


def findSmallestMultiple():
    # probably would be better to just make a factorial function
    r = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
    r = r * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20
    for i in range(2520, r + 1, 2520):
        if checkDivisibility(i):
            print(i)
            break


findSmallestMultiple()
