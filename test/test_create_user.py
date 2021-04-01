import jsonpickle

from api.user import CreateUser
from config.config import *
from dto.user import *


def test_create_user():
    create = CreateUser(URL)
    data = jsonpickle.encode(User(name=NAME, job=JOB))
    response = create.create_user_request(data=data)
    assert response.status_code == 201
