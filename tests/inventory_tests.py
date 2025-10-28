# tests/test_login.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_login_agregar_producto():
    #Login para usar la web
    LoginPage.login_completo

    #Agregar el primer producto al carrito
    InventoryPage.agregar_primer_producto

    #Ir al Carrito
    InventoryPage.ir_al_carrito

    #Obtener los nombres de los productos en el carrito.
    CartPage.obtener_nombres_productos



