def sum_square_difference():
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += i * i
    square_of_sum = 0
    for i in range(1, 101):
        square_of_sum += i
    square_of_sum *= square_of_sum
    print(square_of_sum - sum_of_squares)


sum_square_difference()
