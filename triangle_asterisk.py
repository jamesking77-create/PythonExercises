user_input = int(input("enter a number: "))


def my_triangle(user_number):
    for i in range(1, user_number, 3):
        i = i * "*"
        print(f"{i:>{user_number}}")


my_triangle(user_input)
print()

user_input2 = int(input("enter a number: "))


def my_right_angle_triangle(user_number):
    for i in range(1, user_number, 3):
        i = i * "*"
        print(i)


my_right_angle_triangle(user_input2)
print()

user_input3 = int(input("enter a number: "))


def my_diamond(user_numbers):
    for i in range(user_numbers, 0, -2):
        print(f"{'*' * i:>{i}} ")

    for k in range(1, user_numbers, 2):
        asterisks = k * "*"
        print(asterisks.center(user_numbers))

    for j in range(user_numbers, 0, -2):
        asterisks = j * "*"
        print(asterisks.center(user_numbers))


my_diamond(user_input3)

uer_input4 = int(input("enter a number: "))


def square(user_number):
    for k in range(1, user_number + 3):
        k = "*"
        print(k, end=" ")
    print()
    for i in range(1, user_number):
        i = "*"
        print(i, end=" ")
        print(f"{i:>{user_number * 2 + 1}}")
    for k in range(1, user_number + 3):
        k = "*"
        print(k, end=" ")


square(uer_input4)
