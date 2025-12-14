import requests

#Ver usuario
def test_get_user(url_base, api_headers):
    response = requests.get(f"{url_base}/2", headers=api_headers)
    assert response.status_code == 200

#Crear nuevo usuario
def test_create_user(url_base, api_headers):
    payload = {"name": "Juan", "job": "Tester"}
    response = requests.post(url_base, json=payload, headers=api_headers)
    assert response.status_code == 201

#Eliminar usuario
def test_delete_user(url_base, api_headers):
    response = requests.delete(f"{url_base}/2", headers=api_headers)
    assert response.status_code == 204

#Mostrar usuarios en la 2da página
def test_list_users_page_2(url_base, api_headers):
    response = requests.get(f"{url_base}?page=2", headers=api_headers)

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0

    # Validar campos del primer usuario
    user = data["data"][0]
    assert "id" in user
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user

#Probar login exitoso en reqres
def test_login_success(api_headers):
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url, json=payload, headers=api_headers)

    assert response.status_code == 200

    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str)
