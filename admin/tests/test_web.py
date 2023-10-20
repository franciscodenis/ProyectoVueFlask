from tests import client


def test_web():
    response = client.get("/")
    assert b"Inicio" in response.data
