from src.core import users

def run():
    admin = users.create_user(
        email="admin@test.com",
        username="admin",
        password="adminpassword",
        active=True,
        first_name="System",
        last_name="Admin"
    )
