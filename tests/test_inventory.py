# tests/test_login.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

def test_login_agregar_producto():
    #Login para usar la web
    LoginPage.login_completo
    logger.info("Login realizado con éxito")
    #Agregar el primer producto al carrito
    InventoryPage.agregar_primer_producto
    logger.info("Producto agregado con éxito")
    #Ir al carrito
    InventoryPage.ir_al_carrito

    #Confirmar que el producto está en el carrito (Revisar función en /inventory_page.py)
    InventoryPage.confirmar_productos_carrito


