import requests


def user_request(body):
    return requests.post("https://reqres.in/" + "api/users", data=body)
