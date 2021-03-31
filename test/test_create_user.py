import jsonpickle
import pytest

from dto.user import User
from core.rest_client import *

id = None


@pytest.fixture(scope="session")
def test_create_user():
    response = user_request(jsonpickle.encode(User(name=USER, job=JOB)))
    global id
    id = response.json()["id"]
    assert response.status_code == 201
    assert isinstance(id, str)

    return id


def test_update_user():
    response = get_single_user(str(id))
    assert response.status_code == 200
