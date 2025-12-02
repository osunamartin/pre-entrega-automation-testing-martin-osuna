import pytest, pathlib
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="function")
def driver():
	#Fixture que proporciona un WebDriver configurado.
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

#Supuestamente agrega la URL de la página al reporte HTML de pytest, pero no funciona xd.
def pytest_html_results_table_header(cells):
	"""Añade una columna 'URL' justo después de 'Test ID'."""
	cells.insert(2, 'URL')
def pytest_html_results_table_row(report, cells):
	"""Rellena la columna con la URL almacenada en el atributo
	'page_url'."""
	cells.insert(2, getattr(report, 'page_url', '-'))

#Carpeta para capturas de pantalla
target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True) # Crea carpeta si no existe

#Esto no trae ninguna imagen en el reporte cuando falla, revisar también.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Siempre empieza como None para evitar UnboundLocalError
    driver = None
    file_name = None

    # Solo en fallos de la fase principal
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            file_name = target / f"{item.name}.png"
            driver.save_screenshot(str(file_name))

    # Adjuntar al reporte HTML
    if hasattr(report, 'extra') and file_name:
        report.extra.append({
            'name': 'screenshot',
            'format': 'image',
            'content': str(file_name)
        })

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
      return {"x-api-key": "reqres-free-v1"}
