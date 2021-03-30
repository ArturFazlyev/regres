import jsonpickle

from dto.user import User
from manager.config import *
from service.user_request import user_request
from service.user_response import *


def test_create_user():
    response = user_request(jsonpickle.encode(User(name=USER, job=JOB)))
    user_create_response(response)
