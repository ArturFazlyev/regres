import jsonpickle

from data.user import User
from service.user_request import user_request


def test_create_user():
    response = user_request(jsonpickle.encode(User(name="Joe", job="QA")))
    assert response.status_code == 201
    assert isinstance(response.json()["id"], str)