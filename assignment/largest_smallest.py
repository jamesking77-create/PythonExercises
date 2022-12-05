user_input = int(input(" Please enter a number (enter 0 to quit ): "))
largest_number = smallest_number = user_input
while user_input != 0:
    if user_input > largest_number:
        largest_number = user_input
        if user_input < smallest_number:
            smallest_number = user_input
    user_input = int(input(" Please enter a number (enter 0 to stop): "))
print(" largest number is:", largest_number)
print(" smallest number is:", smallest_number)

