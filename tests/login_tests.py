import pytest
from pages.login_page import *

'''
def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    
    # 1. Ir a la página de login
    login_page.abrir()
    
    # 2. Completar credenciales válidas y hacer login
    login_page.login_completo("standard_user", "secret_sauce")
    
    # 3. Verificar que redirige correctamente
    assert "inventory" in driver.current_url


def test_login_invalido(driver):
    login_page = LoginPage(driver)
    
    # 1. Ir a la página
    login_page.abrir()
    
    # 2. Intentar loguearse con credenciales incorrectas
    login_page.login_completo("usuario_falso", "clave_invalida")
    
    # 3. Verificar que aparece mensaje de error
    assert login_page.esta_error_visible()
    assert "Username and password do not match" in login_page.obtener_mensaje_error()
'''
CASOS_LOGIN = [
    ("standard_user", "secret_sauce", True), # usuario válido, login exitoso
    ("locked_out_user", "secret_sauce", False), # usuario bloqueado,login falla
    ("usuario_malo", "password_malo", False), # credenciales inválidas, login falla
]

@pytest.mark.parametrize("usuario, clave, debe_funcionar",
CASOS_LOGIN)
def test_login_parametrizado(driver, usuario, clave, debe_funcionar):
    login = LoginPage(driver)
    login.abrir()
    login.completar_usuario(usuario)
    login.completar_clave(clave)
    login.hacer_clic_login()

    if debe_funcionar:
    # Si debe funcionar, verificamos que llegamos al inventario
        assert "inventory.html" in driver.current_url
    else:
    # Si no funciona, que falle y nos de el mensaje de error
        pytest.fail(login.obtener_mensaje_error())

