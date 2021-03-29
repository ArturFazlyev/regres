import jsonpickle

from data.user import User
from manager.config import Config
from service.user_request import user_request
from service.user_response import user_create_response


def test_create_user():
    config = Config()
    response = user_request(jsonpickle.encode(User(name=config.get_user(), job=config.get_job())))
    user_create_response(response)
    print(response.json())