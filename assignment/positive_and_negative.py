numbers_of_positive = 0
numbers_of_negative = 0
total = 0
average = 0
user_input = int(input("Enter a number or enter 0 to quit: "))
if user_input == 0:
    print("No number were entered except 0")
while user_input != 0:
    if user_input < 0:
        numbers_of_negative += 1
    if user_input > 0:
        numbers_of_positive += 1
    total = total + user_input/1
    sum_of_total = numbers_of_positive + numbers_of_negative
    average = total / sum_of_total
    user_input = int(input("Enter a number or enter 0 to quit: "))
print(f' The numbers of positive is {numbers_of_positive}\n The numbers of negative is {numbers_of_negative}\n'
      f' The total is {total}\n The average is', round(average, 2))
