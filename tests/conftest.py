import pytest
import pathlib
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pytest_html import extras


# =========================
# CONFIGURACIÓN SELENIUM
# =========================

@pytest.fixture(scope="function")
def driver(request):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Para CI/CD
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    time.sleep(1)
    driver.quit()


# =========================
# FIXTURES API
# =========================

@pytest.fixture
def url_base():
    """
    Base URL para tests de API (ReqRes)
    """
    return "https://reqres.in/api/users"


# =========================
# PYTEST-HTML CONFIG
# =========================

# Carpeta para screenshots
target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)


def pytest_html_results_table_header(cells):
    """
    Agrega columna URL al reporte HTML
    """
    cells.insert(2, "URL")


def pytest_html_results_table_row(report, cells):
    """
    Muestra la URL capturada durante el test
    """
    cells.insert(2, getattr(report, "page_url", "-"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Toma screenshot SOLO si el test falla
    y lo adjunta al reporte HTML
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            file_name = target / f"{item.name}.png"
            driver.save_screenshot(str(file_name))

            report.extras = getattr(report, "extras", [])
            report.extras.append(extras.image(str(file_name)))


@pytest.fixture
def api_headers():
    return {
        "x-api-key": "reqres_3ab6740f4672424f868ab877f5963061", #ApiKey generada en Reqres
        "Content-Type": "application/json"
    }

