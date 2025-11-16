import requests
from jsonschema import validate

from resources.schemas import *

URL = "https://reqres.in/api"
API_KEY = "reqres-free-v1"


# GET + 200 + Валидация элемента data (отдельного user) по schema
def test_get_single_user():
    response = requests.get(f"{URL}/users/2",
                            headers={"x-api-key": API_KEY})
    body = response.json()
    user = body["data"]

    assert response.status_code == 200
    validate(user, schema=get_single_user)


# POST + 201 + Валидация по schema
def test_create_new_user():
    response = requests.post(f"{URL}/users",
                             headers={"x-api-key": API_KEY},
                             json={"name": "morpheus", "job": "leader"})
    body = response.json()

    assert response.status_code == 201
    validate(body, schema=post_user)


# PUT + Валидация по schema
def test_change_user():
    response = requests.put(f"{URL}/users/2",
                            headers={"x-api-key": API_KEY},
                            json={"name": "morpheus", "job": "zion resident"})

    body = response.json()

    assert response.status_code == 200
    validate(body, schema=put_user)


# DELETE + 204
def test_delete_user():
    response = requests.delete(f"{URL}/users/2",
                               headers={"x-api-key": API_KEY})

    assert response.status_code == 204


# Позитивная проверка Resource + Валидация по schema
def test_get_single_resource():
    response = requests.get(f"{URL}/unknown/2",
                            headers={"x-api-key": API_KEY})
    body = response.json()
    resource = body["data"]

    assert response.status_code == 200
    validate(resource, schema=get_single_resource)


# Негативная проверка Resource + 404
def test_not_found_single_resource():
    response = requests.get(f"{URL}/unknown/23",
                            headers={"x-api-key": API_KEY})

    assert response.status_code == 404


# 400 ошибка + Валидация по schema
def test_bad_request_register():
    response = requests.post(f"{URL}/register",
                             headers={"x-api-key": API_KEY},
                             json={"email": "sydney@fife"})
    body = response.json()

    assert response.status_code == 400
    validate(body, schema=error)


# Валидация названия цветов в Resources
def test_validate_resources_colour_names():
    response = requests.get(f"{URL}/unknown",
                            headers={"x-api-key": API_KEY})
    expected_values = {"cerulean", "fuchsia rose", "true red", "aqua sky", "tigerlily", "blue turquoise"}
    body = response.json()
    colour_names = [element["name"] for element in body["data"]]

    assert response.status_code == 200
    assert expected_values == set(colour_names)
