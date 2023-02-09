class Entry:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body

    def set_title(self, title) -> None:
        self.title = title

    def get_title(self) -> str:
        return self.title

    def set_body(self, body) -> None:
        self.body = body

    def get_body(self) -> str:
        return self.body
