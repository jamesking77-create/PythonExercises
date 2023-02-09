from phonebook_app.contact import Contact


class Phonebook:
    contacts = []

    def __init__(self):
        self.contacts = []

    def add_new_contact(self, name: str, number: str, email: str) -> None:
        self.validate_email_address(email)
        self.validate_phone_number(number)
        contact: Contact = Contact(name, number, email)
        self.contacts.append(contact)

    def amount_of_contact(self) -> int:
        return len(self.contacts)

    def view_contact(self, keyword: str) -> str:
        for contact in self.contacts:
            if keyword in contact.get_name() or keyword in contact.get_phone_number() or keyword in contact.get_email():
                contact_info = f"""
                ---------------------------------------
                NAME -> {contact.get_name()}
                ---------------------------------------
                PHONE NUMBER -> {contact.get_phone_number()}
                ---------------------------------------
                EMAIL -> {contact.get_email()}
                ---------------------------------------
                """
                return contact_info

    def count_contact(self) -> int:
        return len(self.contacts)

    def edit_contact_name(self, keyword: str, new_name: str) -> None:
        for contact in self.contacts:
            if keyword in contact.get_name() or keyword in contact.get_phone_number() or keyword in contact.get_email():
                contact.set_name(new_name)

    def edit_contact_number(self, keyword: str, new_number: str) -> None:
        self.validate_phone_number(new_number)
        for contact in self.contacts:
            if keyword in contact.get_name() or keyword in contact.get_phone_number() or keyword in contact.get_email():
                contact.set_phone_number(new_number)

    def edit_contact_email(self, keyword: str, new_email: str) -> None:
        self.validate_email_address(new_email)
        for contact in self.contacts:
            if keyword in contact.get_name() or keyword in contact.get_phone_number() or keyword in contact.get_email():
                contact.set_email(new_email)

    def validate_phone_number(self, number: str) -> None:
        alphabet_list = ["a", "b", "c", "d", "e", "f",
                         "g", "m", "h", "i", "j", "k", "l",
                         "m", "n", "o", "p", "q", "r", "s", "t",
                         "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E",
                         "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                         "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for letter in alphabet_list:
            for digit in number:
                if digit == letter:
                    raise ValueError("invalid number")
                elif len(number) > 11:
                    raise ValueError("invalid number length")

    def validate_email_address(self, email: str) -> None:
        email_annotation1, email_annotation2 = "@yahoo.com", "@gmail.com"
        if email_annotation1 not in email and email_annotation2 not in email:
            raise ValueError("invalid email address...")

    def delete_contact(self, keyword: str) -> None:
        for contact in self.contacts:
            if keyword == contact.get_name() or keyword == contact.get_phone_number() or keyword == contact.get_email():
                self.contacts.remove(contact)
