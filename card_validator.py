def confirm_card(card_numbers):
    if card_numbers.__getitem__(0) == '5':
        card_type = "Master card"
        print(f"Credit Card Type: {card_type} ")
        print(f"Credit Card Number: {card_numbers}")
        print(f"Credit Card Length: {len(card_numbers)}")

    if card_numbers.__getitem__(0) == '4':
        card_type = "Visa Card"
        print(f"Credit Card Type: {card_type} ")
        print(f"Credit Card Number: {card_numbers}")
        print(f"Credit Card Length: {len(card_numbers)}")

    if card_numbers.__getitem__(0) != '4' and card_numbers.__getitem__(0) != '5':
        card_type = 'Invalid...'
        print(f" Credit Card Type: {card_type}")
        print(f"Credit Card Number: {card_numbers}")
        print(f"Credit Card Length: {len(card_numbers)}")


def calculate_card_number(card_numbers):
    sum_digit = 0
    sum_digit2 = 0
    number_list = []
    for digit in card_numbers:
        number_list.append(int(digit))

    for j in range(0, len(card_numbers), 2):
        multiply_digit = number_list[j] * 2
        if multiply_digit > 9:
            multiply_digit = multiply_digit - 9
        sum_digit = sum_digit + multiply_digit

    for k in range(1, len(card_numbers), 2):
        sum_digit2 = sum_digit2 + number_list[k]
    total = sum_digit + sum_digit2
    if total % 10 == 0:
        card_numbers = 'Valid'
    else:
        card_numbers = 'Invalid'
    print(f"Credit Card Status: {card_numbers}")
