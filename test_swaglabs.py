from helpers import *
from selenium.webdriver.common.by import By


driver = iniciar_driver()

try:
    # 1) Login
    login(driver)

    # 2) Validar título de la página e URL
    header_title = driver.find_element(
        By.CSS_SELECTOR, "div.header_secondary_container .title"
    ).text
    assert header_title == "Products", f"Título inesperado: {header_title}"
    assert "/inventory.html" in driver.current_url

    # 3) Verificar que exista al menos un producto
    productos = obtener_productos(driver)
    assert len(productos) > 0, "No se encontraron productos en el inventario"

    # 4) Capturar nombre y precio del primer producto
    first_name = productos[0].find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    first_price = productos[0].find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    print(f"Primer producto → {first_name} – {first_price}")

    # 5) Agregar producto al carrito y comprobar que esté
    agregar_producto_al_carrito(driver)
    print(f"{first_name} agregado al carrito")

    ir_al_carrito(driver)
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert first_name == product_name, "El producto en el carrito no coincide"

    # Validar que el contador del carrito coincide con los productos agregados
    items_en_carrito = obtener_items_en_carrito(driver)
    cart_count = obtener_contador_carrito(driver)
    assert cart_count == len(items_en_carrito), "El contador del carrito no coincide"

    # 6) Resetear la aplicación al estado inicial
    resetear_aplicacion(driver)

finally:
    driver.quit()
