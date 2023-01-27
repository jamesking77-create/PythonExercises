from enum import Enum


class CreditCardType(Enum):
    VISA_CARD = '4'
    MASTER_CARD = '5'
    AMERICA_EXPRESS = '37'
    DISCOVERY_CARD = '6'

    content: str

    def __init__(self, content2: str):
        self.content = content2
