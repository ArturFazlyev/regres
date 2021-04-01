from config.config import *
from core.rest_client import RestClient

create_user = CREATE_USER
get_single_user = GET_SINGLE_USER


class CreateUser(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(CreateUser, self).__init__(api_root_url, **kwargs)

    def create_user_request(self, data):
        return self.post(create_user, data=data)

    def get_single_user(self):
        return self.get(get_single_user)

    def update_user(self, data):
        return self.put(get_single_user, data)