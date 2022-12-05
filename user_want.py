count = 0
user_input = 0
yes = 1
no = 2
largest_number = float("-inf")
smallest_number = float("+inf")
while user_input != 2:
    user_input = int(input(" Enter a number: "))
    user_input2 = int(input(" would you like to add a number: 1 (yes)  or 2 (no): "))
    count += 1
    if user_input > largest_number:
        largest_number = user_input
    if user_input < smallest_number:
        smallest_number = user_input
    if user_input2 == 2:
        print(largest_number, "Is the largest number...")
        print(smallest_number, "is the smallest number...")
        break







