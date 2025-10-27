# tests/test_login.py
import pytest
from pages.login_page import *

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