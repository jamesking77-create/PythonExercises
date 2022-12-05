days = ""
day = ""

current_day = int(input("Enter today's day: "))
while current_day > 6 or current_day < 0:
    current_day = int(input("Wrong input!\nEnter today's day: "))

if current_day == 0:
    days = "Sunday"
if current_day == 1:
    days = "Monday"
if current_day == 2:
    days = "Tuesday"
if current_day == 3:
    days = "Wednesday"
if current_day == 4:
    days = "Thursday"
if current_day == 5:
    days = "Friday"
if current_day == 6:
    days = "Saturday"

new_day = int(input("Enter the number of days elapsed since today: "))
future_day = (current_day + new_day) % 7
if future_day == 0:
    day = "Sunday"
elif future_day == 1:
    day = "Monday"
elif future_day == 2:
    day = "Tuesday"
elif future_day == 3:
    day = "Wednesday"
elif future_day == 4:
    day = "Thursday"
elif future_day == 5:
    day = "Friday"
elif future_day == 6:
    day = "Saturday"
if future_day == 7:
    future_day = 0
print(f"Today is {days} Future day is {day} ")
