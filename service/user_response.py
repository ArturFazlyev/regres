def user_create_response(response):
    assert response.status_code == 201
    assert isinstance(response.json()["id"], str)


def return_user_id(response):
    return str(response.json()["id"])
