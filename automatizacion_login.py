from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
driver = webdriver.Chrome(options=options)


try:
 # 1) Login
 driver.get('https://www.saucedemo.com')
 driver.find_element(By.ID, 'user-name').send_keys('standard_user')
 driver.find_element(By.ID, 'password').send_keys('secret_sauce')
 driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

 
 # 2) Validación del login exitoso y de que estmaos en la pestaña inventory.
 assert '/inventory.html' in driver.current_url
 print('Login exitoso, estamos en Inventory')
 
finally:
 driver.quit()