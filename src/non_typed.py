import json
from pathlib import Path




def get_users_data():
    return json.loads(Path("data", "data.json").read_text())


def get_max_age(users):
    ages = [user["age"] for user in users]
    return max(ages)
