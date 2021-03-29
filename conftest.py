import jsonpickle
import pytest

from dto.user import User
from manager.config import Config
from service.user_request import user_request
from service.user_response import *

id = None

@pytest.fixture(autouse=True)
def app():
    global id
    config = Config()
    response = user_request(jsonpickle.encode(User(name=config.get_user(), job=config.get_job())))
    user_create_response(response)
    id = return_user_id(response)
