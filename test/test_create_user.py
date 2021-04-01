from http import HTTPStatus

import jsonpickle
from assertpy import assert_that

from api.user import CreateUser
from config.config import *
from dto.user import *

create = CreateUser(URL)


def test_create_user():
    data = jsonpickle.encode(User(name=NAME, job=JOB))
    response = create.create_user_request(data=data)
    assert_that(response.status_code).is_equal_to(HTTPStatus.CREATED)
    assert_that(isinstance(response.json()["id"], str)).is_equal_to(True)


def test_update_user():
    data = jsonpickle.encode(User(name="morp", job="QA Automation"))
    response = create.update_user(data=data)
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(isinstance(response.json()["updatedAt"], str)).is_equal_to(True)


def test_get_user():
    response = create.get_single_user()
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
