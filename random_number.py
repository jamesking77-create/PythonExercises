import random
number_to_be_guessed = random.randint(1, 100)
number_of_guesses = 0
while number_of_guesses < 3:
    number_of_guesses = int(input("Please enter a number between 1 to 100: "))
    if number_of_guesses == number_to_be_guessed:
        print("You got it right!!!")
        number_of_guesses = number_of_guesses + 1
        break
    else:
        guess = int(input("Please enter a number between 1 to 100: "))
print("Try again later , the lucky number is ", number_to_be_guessed)