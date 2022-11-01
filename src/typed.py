import json
from pathlib import Path

from src.annotations import User


def get_users_data() -> list[User]:
    return json.loads(Path("data", "data.json").read_text())


def get_max_age(users: list[User]) -> int:
    ages = [user["age"] for user in users]
    return max(ages)
