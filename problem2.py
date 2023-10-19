a = 1
b = 2
sum = 2
while b < 4000000:
    temp = a
    a = b
    b = b + temp
    if b % 2 == 0:
        sum += b
print(sum)
