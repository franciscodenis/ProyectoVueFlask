from src.core import user

def run():
    admin = user.create_user(
        email="admin@test.com",
        username="admin",
        password="adminpassword",
        active=True,
        first_name="System",
        last_name="Admin"
    )
