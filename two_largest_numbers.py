largest_number = float("-inf")
second_largest_number = float("+inf")
count = 0
while count <= 4:
    number_of_input = int(input("Please enter a number: "))
    count = count + 1
    if number_of_input > largest_number:
        second_largest_number = largest_number
        largest_number = number_of_input
    if second_largest_number < largest_number:
        second_largest_number = number_of_input
print("your largest number is ", largest_number)
print("your second largest number is ", second_largest_number)

# count = 0
# for count in range(1, 5, 3):
#     if count == 4:
#         print("you doubt alot ")
#     else:
#         print("i could have kill alot....")

# word = "james, yk, prof"
# for x in word:
#     print(x)


