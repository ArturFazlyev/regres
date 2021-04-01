from config.config import *
from core.rest_client import RestClient

api_root_url = URL
create_user = CREATE_USER
get_single_user = GET_SINGLE_USER


class CreateUser(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(CreateUser, self).__init__(api_root_url, **kwargs)

    def create_user_request(self, data, **kwargs):
        return self.post(create_user, data=data, **kwargs)

    def get_single_user(self, id, **kwargs):
        return self.get(get_single_user.format(id), **kwargs)
