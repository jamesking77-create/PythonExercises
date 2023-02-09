from assignment_.diary_app_package.entry import Entry


class Diary:
    entries = []

    def __init__(self):
        self.entries = []

    def create_entry(self, title: str, body: str) -> None:
        entry: Entry = Entry(title, body)
        self.entries.append(entry)

    def number_of_entries(self) -> int:
        return len(self.entries)

    def view_entry(self, ID: int) -> str:
        identifier = ID - 1
        self.validate_ID(identifier)
        entry_info = f""""
        --------------------------------
        TITLE: {self.entries.__getitem__(identifier).get_title()}
        --------------------------------
        BODY: {self.entries.__getitem__(identifier).get_body()}
        --------------------------------
        """
        return entry_info

    def validate_ID(self, ID: int) -> None:
        if ID < 0 or ID > len(self.entries):
            raise ValueError

    def count_entry(self) -> int:
        return len(self.entries)

    def edit_entry_title(self, ID: int, new_title: str) -> None:
        identifier = ID - 1
        self.validate_ID(identifier)
        self.entries.__getitem__(identifier).set_title(new_title)

    def edit_entry_body(self, ID: int, new_body: str) -> None:
        identifier = ID - 1
        self.validate_ID(identifier)
        self.entries.__getitem__(identifier).set_body(new_body)

    def delete_entry(self, ID) -> None:
        identifier = ID - 1
        self.validate_ID(identifier)
        self.entries.remove(self.entries.__getitem__(identifier))

