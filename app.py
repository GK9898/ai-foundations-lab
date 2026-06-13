users_database = [

{"id": 101, "name": "Alice", "role": "admin", "is_active": True},

{"id": 102, "name": "Bob", "role": "user", "is_active": False},

{"id": 103, "name": "Charlie", "role": "editor", "is_active": True}

]

active_user = [user['name'] for user in users_database if user["is_active"] == True]
print(active_user)