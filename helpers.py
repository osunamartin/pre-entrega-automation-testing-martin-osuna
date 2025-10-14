from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def iniciar_driver():
    #Inicializa y devuelve el driver de Chrome.
    options = Options()
    driver = webdriver.Chrome(options=options)
    return driver


def login(driver, username="standard_user", password="secret_sauce"):
    #Realiza el login en SauceDemo con credenciales por defecto.
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


def obtener_productos(driver):
    #Devuelve una lista de elementos de productos disponibles en el inventario.
    return driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")


def agregar_producto_al_carrito(driver, product_id="add-to-cart-sauce-labs-backpack"):
    #Agrega un producto al carrito usando su ID de botón.
    driver.find_element(By.ID, product_id).click()


def ir_al_carrito(driver):
    #Navega hasta el carrito de compras.
    driver.find_element(By.ID, "shopping_cart_container").click()


def obtener_items_en_carrito(driver):
    #Devuelve la lista de productos en el carrito.
    return driver.find_elements(By.CLASS_NAME, "cart_item")


def obtener_contador_carrito(driver):
    #Devuelve el número que aparece en el ícono del carrito.
    return int(driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)


def resetear_aplicacion(driver):
    #Reinicia la aplicación a su estado original desde el menú lateral.
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)  # Espera a que el menú lateral aparezca
    driver.find_element(By.ID, "reset_sidebar_link").click()
