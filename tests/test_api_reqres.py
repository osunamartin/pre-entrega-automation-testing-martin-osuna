import requests
import pytest

def test_get_user(url_base, header_request):
   

    response = requests.get(f"{url_base}/2", headers=header_request)

    assert response.status_code == 200
    data = response.json()

    assert data["data"]["id"] == 2

def test_create_user(url_base, header_request):
    payload = {"name": "morpheus", "job": "leader"}

    response = requests.post(url_base, headers=header_request, json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == payload["name"]
    
def test_delete_user(url_base, header_request):
    response = requests.delete(f"{url_base}/2", headers=header_request)

    assert response.status_code == 204