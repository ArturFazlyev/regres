from core.rest_client import RestClient


class User(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super.__init__(api_root_url, **kwargs)
