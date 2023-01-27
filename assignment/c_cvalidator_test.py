from unittest import TestCase

from assignment_.card_validation_2.credit_card import CreditCard
from assignment_.card_validation_2.Credit_card_type import CreditCardType


class CreditCardValidatorTest(TestCase):
    def test_odd_number_from_right_to_left_product_sum(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        credit_card.sum_the_product_of_second_digit()
        self.assertEqual(37, credit_card.get_sum_of_second_digit_product())

    def test_sum_of_odd_number(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        credit_card.sum_odd_digits()
        self.assertEqual(38, credit_card.get_sum_of_odd_numbers())

    def test_that_invalid_card_length_throws_exception(self):
        credits_card: CreditCard = CreditCard("43885760184026265768734675")
        with self.assertRaises(ValueError):
            credits_card.validate_card_length()

    def test_card_validity(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        self.assertTrue(credit_card.is_valid())

    def test_card_is_of_four_types_by_first_number(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        credit_card.set_card_type()
        self.assertEqual(CreditCardType.VISA_CARD, credit_card.get_card_type())

    def test_string_representation_of_card_validity(self):
        credit_card: CreditCard = CreditCard("4388576018410707")
        credit_card.validate_card_length()
        credit_card.sum_odd_digits()
        credit_card.sum_the_product_of_second_digit()
        credit_card.set_card_type()
        expected: str = f"""
        =============================================
        Credit CardType: CreditCardType.VISA_CARD
        Credit card Number: 4388576018410707
        Credit Card Length: 16
        Credit Card Status: valid
        =============================================
        """
        self.assertEqual(expected, credit_card.__str__())

