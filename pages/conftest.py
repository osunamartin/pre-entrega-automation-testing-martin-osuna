import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
	"""Fixture que proporciona un WebDriver configurado."""
	chrome_options = Options()
	# chrome_options.add_argument("--headless") # Para CI/CD
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("--disable-dev-shm-usage")

	service = Service()
	driver = webdriver.Chrome(service=service, options=chrome_options)
	driver.maximize_window()
	driver.implicitly_wait(5)

	yield driver

	time.sleep(1) # Para ver el resultado final
	driver.quit()
