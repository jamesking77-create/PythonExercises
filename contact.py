class Contact:
    def __init__(self, name: str, phone_number: str, email_address: str):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def set_name(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_phone_number(self, number) -> None:
        self.phone_number = number

    def get_phone_number(self) -> str:
        return self.phone_number

    def set_email(self, email) -> None:
        self.email_address = email

    def get_email(self) -> str:
        return self.email_address


