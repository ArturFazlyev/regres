import requests

from manager.config import *


def user_request(body):
    return requests.post(URL + CREATE_USER, data=body)
