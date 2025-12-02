import requests
import pytest

@pytest.mark.api
def test_post_users(url_base, header_request): 
    url = f"{url_base}"
    payload = {"name": "morpheus", "job": "leader"}

    response = requests.post(url, headers=header_request, json=payload) 

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == payload["name"]

    assert "id" in data