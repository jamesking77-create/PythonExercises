# user_input = 0

total = 0
count = 0
while count < 100:
    user_input = int(input("Enter a number or enter 0 to quit: "))
    total += user_input
    average = total / 2
    count = count + 1
    if user_input < 0:
        print(user_input, "is a negative number...")
    elif user_input > 0:
        print(user_input, "is a positive number")
    else: break
