import pytest
import requests

URL = "https://reqres.in/api/login"

@pytest.mark.parametrize(
    "email, password, status_esperado, debe_tener_token",
    [
        # Caso válido
        ("eve.holt@reqres.in", "cityslicka", 200, True),

        # Caso inválido → Falta password
        ("eve.holt@reqres.in", None, 400, False),
    ]
)
def test_login_api(email, password, status_esperado, debe_tener_token):
    # Construir el body dinámicamente
    payload = {"email": email}
    if password is not None:
        payload["password"] = password

    # Hacer la solicitud
    response = requests.post(URL, json=payload)

    # Verificar código de estado
    assert response.status_code == status_esperado, \
        f"Se esperaba código {status_esperado}, pero llegó {response.status_code}"

    data = response.json()

    # Verificar si corresponde token
    if debe_tener_token:
        assert "token" in data, "La respuesta debería contener un token y no lo contiene"
        print(f"✅ Login correcto. Token: {data['token']}")
    else:
        assert "token" not in data, "No debería haber token en caso de error"
        print(f"⚠️ Login inválido, respuesta: {data}")
