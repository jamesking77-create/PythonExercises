from phonebook_app.phonebook import Phonebook

phonebook = Phonebook()


def add_new_contact():
    try:
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email_address = input("Enter email address: ")
        phonebook.add_new_contact(name, phone_number, email_address)
        print("Contact added successfully")
        back_button = input("1 -> BACK TO MENU: ")
        match back_button:
            case "1":
                phonebook_menu()
        while back_button != "1":
            back_button = input("1 -> BACK TO MENU: ")
            if back_button == "1":
                phonebook_menu()
        phonebook_menu()
    except ValueError:
        print("wrong input")
        phonebook_menu()


def find_contact():
    try:
        search_keyword = input("Search for contact: ")
        print(phonebook.view_contact(search_keyword))
        back_button = input("1 -> BACK TO MENU: ")
        match back_button:
            case "1":
                phonebook_menu()
        while back_button != "1":
            back_button = input("1 -> BACK TO MENU: ")
            if back_button == "1":
                phonebook_menu()
    except ValueError:
        print("Contact does not exist")


def edit_contact():
    search_keyword = input("Search for contact: ")
    edit_drop_down = input("""
    ---------------------------------
    1 -> EDIT CANTACT NAME
    2 -> EDIT PHONE NUMBER
    3 -> EDIT EMAIL ADDRESS
    ---------------------------------
    """)

    match edit_drop_down:
        case "1":
            new_name = input("enter contact new name: ")
            print(phonebook.view_contact(search_keyword))
            phonebook.edit_contact_name(search_keyword, new_name)
            print("Your contact ( name ) have been updated...")
            print(phonebook.view_contact(new_name))
            back_button = input("1 -> BACK TO MENU: ")
            match back_button:
                case "1":
                    phonebook_menu()
            while back_button != "1":
                back_button = input("1 -> BACK TO MENU: ")
                if back_button == "1":
                    phonebook_menu()
        case "2":
            new_number = input("enter contact new phone number: ")
            # phonebook.validate_phone_number(new_number)
            print(phonebook.view_contact(search_keyword))
            phonebook.edit_contact_number(search_keyword, new_number)
            print("Your contact ( number ) have been updated...")
            print(phonebook.view_contact(new_number))
            back_button = input("1 -> BACK TO MENU: ")
            match back_button:
                case "1":
                    phonebook_menu()
            while back_button != "1":
                back_button = input("1 -> BACK TO MENU: ")
                if back_button == "1":
                    phonebook_menu()
        case "3":
            new_email = input("enter contact new email address: ")
            # phonebook.validate_email_address(new_email)
            print(phonebook.view_contact(search_keyword))
            phonebook.edit_contact_email(search_keyword, new_email)
            print("Your contact ( email ) have been updated...")
            print(phonebook.view_contact(new_email))
            back_button = input("1 -> BACK TO MENU: ")
            match back_button:
                case "1":
                    phonebook_menu()
            while back_button != "1":
                back_button = input("1 -> BACK TO MENU: ")
                if back_button == "1":
                    phonebook_menu()


def count_contact():
    print(f"you have {phonebook.amount_of_contact()} contact in your contact list")
    phonebook_menu()


def delete_contact():
    try:
        search_contact = input("search for contact to ( DELETE )")
        print(phonebook.view_contact(search_contact))
        confirmation = input("TYPE yes -> TO CONFIRM DELETE: ")
        match confirmation:
            case "yes":
                phonebook.delete_contact(search_contact)
                print("contact has been deleted successfully...")
                if confirmation != "yes":
                    phonebook_menu()
    except ValueError:
        print("contact does not exist...")


def exit_phonebook():
    exit(0)


def phonebook_menu():
    menu = input("""
    -----------------------------
    1 -> ADD CONTACT
    2 -> FIND CONTACT
    3 -> EDIT CONTACT
    4 -> COUNT CONTACT
    5 -> DELETE CONTACT
    6 -> CLOSE PHONEBOOK
    ----------------------------- 
    """)
    match menu:
        case "1":
            add_new_contact()
        case "2":
            find_contact()
        case "3":
            edit_contact()
        case "4":
            count_contact()
        case "5":
            delete_contact()
        case "6":
            exit_phonebook()
        case other:
            phonebook_menu()


if __name__ == '__main__':
    phonebook_menu()
