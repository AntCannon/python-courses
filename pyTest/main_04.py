class Database:
    """Simulates a basic user database"""

    def __init__(self):
        self.data = {}  # Simulating an in memory database

    def __str__(self):
        return f"{self.data}"

    def add_user(self, user_id: int, name: str) -> None:
        if user_id in self.data:
            raise ValueError("User ID already exists")

        if name in self.data.values():
            raise ValueError("User Name already exists")

        self.data[user_id] = name

    def get_user(self, user_id: int) -> str | None:
        if not user_id in self.data:
            raise ValueError("User does not exist")
        return self.data.get(user_id, None)

    def delete_user(self, user_id: int) -> None:
        if not user_id in self.data:
            raise ValueError("User does not exist")
        del self.data[user_id]
