lucky_number = 17
number_of_guesses = 0
count = 0
while count < 4:
    number_of_guesses = int(input("Please enter a number: "))
    count = count + 1
    if number_of_guesses > lucky_number:
        print("sorry your number is greater than the lucky number!!!")
    if number_of_guesses < lucky_number:
        print("sorry your number is lower than the lucky number!!!")
    if number_of_guesses == lucky_number:
        print("Hurray you won!!!")

print("Game over!!!, ", lucky_number, " is the lucky number")