import requests

from manager.config import Config

config = Config()


def user_request(body):
    return requests.post(config.get_url() + config.get_create_user(), data=body)
