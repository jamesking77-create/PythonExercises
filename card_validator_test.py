from card_validator import *
if __name__ == '__main__':
    user_card = str(input("Enter you card number for verification please: "))
    confirm_card(user_card)
    calculate_card_number(user_card)