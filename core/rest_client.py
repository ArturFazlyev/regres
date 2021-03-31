import requests


class RestClient():
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def request(self, url, method, data=None, **kwargs):
        url = self.api_root_url + url
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, **kwargs)
        if method == "PUT":
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            return self.session.patch(url, data, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data, **kwargs):
        return self.request(url, "POST", data, **kwargs)

    def put(self, url, data, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def put(self, url, data, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)