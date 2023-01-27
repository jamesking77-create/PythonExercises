from assignment_.card_validation_2.Credit_card_type import CreditCardType


class CreditCard:

    def __init__(self, credit_card_number: str):
        self.__credit_card_number: str = credit_card_number
        self.sum_digit = 0
        self.sum_odd_digit = 0
        self.card_number_list = []
        self.card_number_list2 = []
        self.credit_card_type: CreditCardType = None

    def sum_the_product_of_second_digit(self) -> None:
        for digit in self.__credit_card_number:
            self.card_number_list.append(int(digit))

        for i in range(0, len(self.card_number_list), 2):
            multiply_digit = self.card_number_list.__getitem__(i) * 2
            if multiply_digit > 9:
                multiply_digit = multiply_digit - 9
            self.sum_digit = self.sum_digit + multiply_digit

    def get_sum_of_second_digit_product(self) -> int:
        return self.sum_digit

    def sum_odd_digits(self) -> None:
        for digit in self.__credit_card_number:
            self.card_number_list2.append(int(digit))
        for j in range(1, len(self.card_number_list2), 2):
            odd_digits = self.card_number_list2.__getitem__(j)
            self.sum_odd_digit = self.sum_odd_digit + odd_digits

    def get_sum_of_odd_numbers(self) -> int:
        return self.sum_odd_digit

    def validate_card_length(self) -> None:
        if len(self.__credit_card_number) < 13 or len(self.__credit_card_number) > 16:
            raise ValueError

    def is_valid(self) -> bool:
        # print(self.sum_digit + self.sum_odd_digit)
        if (self.sum_digit + self.sum_odd_digit) % 10 == 0:
            return True

    def set_card_type(self) -> None:
        if self.__credit_card_number.__getitem__(0) == "4":
            self.credit_card_type = CreditCardType.VISA_CARD
        elif self.__credit_card_number.__getitem__(0) == '5':
            self.credit_card_type = CreditCardType.MASTER_CARD
        elif self.__credit_card_number.__getitem__(0) == '3' and self.__credit_card_number.__getitem__(1) == '7':
            self.credit_card_type = CreditCardType.AMERICA_EXPRESS
        elif self.__credit_card_number.__getitem__(0) == '6':
            self.credit_card_type = CreditCardType.DISCOVERY_CARD

    def get_card_type(self) -> CreditCardType:
        return self.credit_card_type

    def __str__(self) -> str:
        status: str = ""
        if self.is_valid():
            status = "valid"
        else:
            status = "invalid"

        return f"""
        =============================================
        Credit CardType: {self.credit_card_type}
        Credit card Number: {self.__credit_card_number}
        Credit Card Length: {len(self.__credit_card_number)}
        Credit Card Status: {status}
        =============================================
        """



