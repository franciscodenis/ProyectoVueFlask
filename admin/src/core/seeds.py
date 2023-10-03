from src.core import auth

def run():
    admin = auth.create_user(
        email="admin@test.com",
        username="admin",
        password="1234",
        active=True,
        first_name="System",
        last_name="Admin"
    )
