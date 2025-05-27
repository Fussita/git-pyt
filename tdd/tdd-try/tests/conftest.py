import pytest
from fastapi.testclient import TestClient
from app.main import app

listUsers = [
    ["Pedro Perez", 28],
    ["María Rosales", 26],
    ["Juan Martínez", 32],
    ["Ana Gómez", 24],
]

@pytest.fixture(scope="function")
def client():
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture(scope="module")
def json_headers():
    return {"Content-Type": "application/json"}

@pytest.fixture(scope="module")
def id_user_exists():
    return 24

@pytest.fixture(scope="module")
def users_length():
    return len( listUsers )
