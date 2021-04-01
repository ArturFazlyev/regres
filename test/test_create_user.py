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


def update_user():
    data = jsonpickle.encode(User(name="morp", job="QA Automation"))
    response = create.update_user(data=data)
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json()["updatedAt"], str)


def get_user():
    response = create.get_single_user()
    assert response.status_code == HTTPStatus.OK
