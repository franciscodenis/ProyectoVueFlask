from src.core.users import create_user

def run():
    admin = create_user(
        email="admin@test.com",
        username="admin",
        password="adminpassword",
        active=True,
        first_name="System",
        last_name="Admin"
    )
