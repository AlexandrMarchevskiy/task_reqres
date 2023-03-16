import pytest
import requests


@pytest.fixture(scope="module")
def api_url():
    return "https://reqres.in/api/"


@pytest.fixture(scope="module")
def headers():
    return {"Content-Type": "application/json"}


# Позитивные тесты:
@pytest.mark.parametrize("user_id", [1, 2])
def test_get_user(api_url, user_id, headers):
    response = requests.get(api_url + f"users/{user_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id


def test_create_user(api_url, headers):
    data = {"name": "test_user", "email": "test_user@test.com", "password": "123456"}
    response = requests.post(api_url + "users", json=data, headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == data["name"]


@pytest.mark.parametrize("user_id", [1, 2])
def test_update_user(api_url, user_id, headers):
    data = {"name": "updated_user"}
    response = requests.put(api_url + f"users/{user_id}", json=data, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == data["name"]


@pytest.mark.parametrize("user_id", [1, 2])
def test_delete_user(api_url, user_id, headers):
    response = requests.delete(api_url + f"users/{user_id}", headers=headers)
    assert response.status_code == 204


# Негативные тесты:
def test_create_user_with_empty_name(api_url, headers):
    data = {"name": "", "email": "test_user@test.com", "password": "123456"}
    response = requests.post(api_url + "users", json=data, headers=headers)
    assert response.status_code == 400


def test_get_user_with_invalid_id(api_url, headers):
    response = requests.get(api_url + "users/9999", headers=headers)
    assert response.status_code == 404


def test_update_user_with_empty_name(api_url, headers):
    data = {"name": ""}
    response = requests.put(api_url + "users/1", json=data, headers=headers)
    assert response.status_code == 400


def test_create_user_with_invalid_email(api_url, headers):
    data = {"name": "test_user", "email": "test_user", "password": "123456"}
    response = requests.post(api_url + "users", json=data, headers=headers)
    assert response.status_code == 400