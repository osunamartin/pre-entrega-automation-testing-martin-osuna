import os
from utils.datos import leer_csv_login
import pytest
from pages.login_page import *

ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos', 'login.csv')
ruta_csv = os.path.abspath(ruta_csv)

@pytest.mark.parametrize("usuario, clave, debe_funcionar", leer_csv_login(ruta_csv))
def test_login_parametrizado(driver, usuario, clave, debe_funcionar):
    login = LoginPage(driver)
    login.abrir()
    login.completar_usuario(usuario)
    login.completar_clave(clave)
    login.hacer_clic_login()
    
    if debe_funcionar:
        assert "inventory.html" in driver.current_url
    else:
        assert login.obtener_mensaje_error()