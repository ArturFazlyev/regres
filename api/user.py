from config.config import *
from core.rest_client import RestClient

api_root_url = URL
create_user = CREATE_USER
get_single_user = GET_SINGLE_USER


class User(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super.__init__(api_root_url, **kwargs)

    def create_user(self, data, **kwargs):
        return self.post(create_user, data=data, **kwargs)

    def get_single_user(self, id, **kwargs):
        return self.get(get_single_user.format(id), **kwargs)
