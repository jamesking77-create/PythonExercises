from assignment_.diary_app_package.diary import Diary

diary = Diary()


def create_new_entry():
    try:
        title = input("enter the title: ")
        body = input("oya gist us: ")
        diary.create_entry(title, body)
        print(f"Entry @ ( ID: {diary.number_of_entries()} ) created successfully...")
        back_button = input("1 -> BACK TO MENU: ")
        match back_button:
            case "1":
                diary_menu()
        while back_button != "1":
            back_button = input("1 -> BACK TO MENU: ")
    except ValueError:
        print(ValueError)
        diary_menu()
    finally:
        diary_menu()


def view_entry():
    try:
        I_D = int(input("Enter ( ID ) of entry to view: "))
        print(diary.view_entry(I_D))
        back_button = input("1 -> BACK TO MENU: ")
        match back_button:
            case "1":
                diary_menu()
        while back_button != "1":
            back_button = input("1 -> BACK TO MENU: ")
    except ValueError:
        print("Entry ( ID ) does not exist...")
        diary_menu()
    finally:
        diary_menu()


def edit_entry():
    try:
        I_D = int(input("Enter ( ID ) of entry to edit: "))
        diary.validate_ID(I_D)
        edit_dropdown = input("""
        -----------------------
        1 -> EDIT TITLE
        2 -> EDIT BODY
        -----------------------
        """)
        match edit_dropdown:
            case "1":
                try:
                    print(diary.view_entry(I_D))
                    new_title = input("Enter your new title: ")
                    diary.edit_entry_title(I_D, new_title)
                    print(diary.view_entry(I_D))
                    print("Your entry title updated successfully...")
                    back_button = input("1 -> BACK TO MENU: ")
                    match back_button:
                        case "1":
                            diary_menu()
                    while back_button != "1":
                        back_button = input("1 -> BACK TO MENU: ")
                except ValueError:
                    print(ValueError)
                    diary_menu()

            case "2":
                try:
                    print(diary.view_entry(I_D))
                    new_body = input("Enter your new body: ")
                    diary.edit_entry_body(I_D, new_body)
                    print(diary.view_entry(I_D))
                    print("Your entry body updated successfully...")
                    back_button = input("1 -> BACK TO MENU: ")
                    match back_button:
                        case "1":
                            diary_menu()
                    while back_button != "1":
                        back_button = input("1 -> BACK TO MENU: ")
                except ValueError:
                    print(ValueError)
                    diary_menu()
    except ValueError:
        print("Entry ( ID ) does not exist...")
        diary_menu()
    finally:
        print("wrong input...")
        diary_menu()


def count_entry():
    print(f"you have {diary.number_of_entries()} entry available.")
    back_button = input("1 -> BACK TO MENU: ")
    match back_button:
        case "1":
            diary_menu()
    while back_button != "1":
        back_button = input("1 -> BACK TO MENU: ")


def delete_entry():
    try:
        I_D = int(input("Enter ( ID ) of entry to ( DELETE ): "))
        diary.validate_ID(I_D)
        confirmation = input("TYPE yes -> TO CONFIRM DELETE: ")
        try:
            match confirmation:
                case "yes":
                    diary.delete_entry(I_D)
                    print(f"Entry @ ( ID: {diary.number_of_entries()} ) DELETED successfully..")
                    diary_menu()
            if confirmation != "yes":
                diary_menu()
        except ValueError:
            print("Entry ( ID ) dos not exist.")
    except ValueError:
        print("Entry ( ID ) dos not exist.")
        diary_menu()


def exist_diary():
    print("goodbye diary...")



def diary_menu():
    menu: str = input("""
    ------------------------
    1 -> create new entry
    2 -> view your entry
    3 -> edit your entry
    4 -> count your entry
    5 -> delete your entry
    6 -> close your diary
    ------------------------
    """)
    match menu:
        case "1":
            create_new_entry()
        case "2":
            view_entry()
        case "3":
            edit_entry()
        case "4":
            count_entry()
        case "5":
            delete_entry()
        case "6":
            exist_diary()
        case other:
            diary_menu()
    # if menu != "1" and menu != "2" and menu != "3" and menu != "4" and menu != "5" and menu != "6":
    #     diary_menu()


if __name__ == '__main__':
    print(f"""
     ------------------------
    {"WELCOME":>15}
     ------------------------
    """)
    diary_menu()
