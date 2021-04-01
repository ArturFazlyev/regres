from http import HTTPStatus

import jsonpickle

from api.user import CreateUser
from config.config import *
from dto.user import *

create = CreateUser(URL)


def test_create_user():
    data = jsonpickle.encode(User(name=NAME, job=JOB))
    response = create.create_user_request(data=data)
    assert response.status_code == HTTPStatus.CREATED
    assert isinstance(response.json()["id"], str)


def test_get_single_user():
    response = create.get_single_user()
    assert response.status_code == HTTPStatus.OK
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
    assert response.json()["data"]["first_name"] == "Janet"
    assert response.json()["data"]["last_name"] == "Weaver"

