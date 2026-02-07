def active_user_names(users):
    return sorted([u["name"].upper() for u in users if u.get("active")])

users = [
    {"id": 1, "name": "ola", "active": True},
    {"id": 2, "name": "mike", "active": False},
    {"id": 3, "name": "anna", "active": True},
    {"id": 4, "name": "zoe", "active": True},
]

print(active_user_names(users))
