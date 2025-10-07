from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
driver = webdriver.Chrome(options=options)


try:
 # 1) Login
 driver.get('https://www.saucedemo.com')
 driver.find_element(By.ID, 'user-name').send_keys('standard_user')
 driver.find_element(By.ID, 'password').send_keys('secret_sauce')
 driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

 # 2) Validación del título y de que estamos en la pestaña inventory.
 header_title = driver.find_element(
 By.CSS_SELECTOR, "div.header_secondary_container .title"
 ).text
 assert header_title == "Products", f"Título inesperado: {header_title}"
 assert '/inventory.html' in driver.current_url
 
 # 3) Verificar que exista al menos un producto
 products = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
 assert len(products) > 0, "No se encontraron productos"

 # 4) Capturar nombre y precio del primer producto
 first_name  = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_name").text
 first_price = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_price").text
 print(f"Primer producto → {first_name} – {first_price}")

 # 5) Agregar un producto al carrito
 driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
 print(f"{first_name} agregado al carrito")

 # 6) Reiniciar al estado original de la web
 driver.find_element(By.ID, 'react-burger-menu-btn').click()
 driver.implicitly_wait(3)
 driver.find_element(By.ID, 'reset_sidebar_link').click()
 
finally:
 driver.quit()