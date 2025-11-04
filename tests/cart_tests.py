import os
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def usuario_logueado(driver):
    """
    Fixture que realiza login antes de cada test de carrito
    """
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login_completo("standard_user", "secret_sauce")
    
    # Verificar que el login fue exitoso
    assert "inventory.html" in driver.current_url
    
    return InventoryPage(driver)


def test_agregar_primer_producto_varias_veces(usuario_logueado):
    """
    Test que agrega el primer producto del inventario varias veces
    y verifica que el contador del carrito aumenta correctamente.
    """
    inventory_page = usuario_logueado
    
    contador_inicial = inventory_page.obtener_contador_carrito()
    print(f"Contador antes de agregar producto: {contador_inicial}")

    # Agregar el primer producto
    inventory_page.agregar_primer_producto()

    # Verificar incremento
    contador_final = inventory_page.obtener_contador_carrito()
    print(f"   Contador luego de agregar producto: {contador_final}")

    assert contador_final == contador_inicial + 1
    f"❌ El contador no se incrementó correctamente"

    print(f"\n✅ Se agregó correctamente el producto al carrito  veces.")

