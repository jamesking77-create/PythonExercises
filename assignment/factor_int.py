user_input = int(input('please enter a number: '))
factor = 0
count = 0
for count in range(user_input):
    if user_input % count == 0:
        factor += factor
        count += count
        print(user_input, ' has ', factor, ' factors')
