class User:
    def __init__(self, tracker) -> None:
        self.user_title = tracker.get_slot("user_title") or "anh"
        self.user_name = tracker.get_slot("user_name") or "ạ"

    def get_title(self):
        return self.user_title

    def get_name(self):
        return self.user_name