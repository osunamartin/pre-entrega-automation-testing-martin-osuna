ENG

## 🎯 Test Automation Project – UI (Selenium) and API (ReqRes)

This project includes UI test automation for the SwagLabs (SauceDemo) website and API testing for the public ReqRes API, using Python and Pytest.

Good automation practices are applied, such as Page Object Model (POM), use of fixtures, and HTML report generation.


## 📌 Project Purpose

The objective of this project is:

* Practice and demonstrate knowledge in UI test automation with Selenium
* Implement automated API tests using requests and Pytest
* Apply good design practices such as Page Object Model (POM) for UI
* Centralize configurations and utilities using conftest.py
* Generate clear and visual HTML reports for result analysis


## 🧪 Test Scope

### 🔹 UI Tests – SwagLabs (SauceDemo)

Site: https://www.saucedemo.com

Automated flows:

* User login
* Inventory validation
* Adding products to the cart
* Resetting application state

UI tests are structured using Page Object Model (POM) to improve:

* Readability
* Maintainability
* Code reusability

### 🔹 API Tests – ReqRes

API used: https://reqres.in

Covered endpoints:

* Get user by ID (GET)
* List users (GET)
* Create user (POST)
* Delete user (DELETE)
* Successful login (POST)
* Failed login (POST – negative case)

API tests validate:

* HTTP status codes
* Response structure
* Key data returned by the API

⚠️ Important note: ReqRes currently requires the use of an API Key to access its endpoints.

## 🛠️ Technologies Used

* Python
* Pytest
* Selenium WebDriver
* Requests (for API testing)
* Google Chrome
* ChromeDriver
* pytest-html (reports)

## ⚙️ Installation and Setup

### 1️⃣ Clone the repository

git clone https://github.com/osunamartin/pre-entrega-automation-testing-martin-osuna.git
cd pre-entrega-automation-testing-martin-osuna

### 2️⃣ Create and activate virtual environment

python -m venv venv

Linux / Mac:
source venv/bin/activate

Windows:
venv\Scripts\activate

### 3️⃣ Install dependencies

pip install selenium pytest requests pytest-html

⚠️ Selenium must be version 4.36.0 or higher.

### 4️⃣ Configure ReqRes API Key

Create a free API Key at: 👉 https://app.reqres.in

Then add it in the corresponding fixture (for example, in conftest.py):

@pytest.fixture
def api_headers():
return {
"x-api-key": "YOUR_API_KEY_HERE",
"Content-Type": "application/json"
}


⚠️ Use a valid API key for this step. The author’s key is not included for security reasons.


---
ESP

# Proyecto de Automatización de Pruebas – UI (Selenium) y API (ReqRes)

Este proyecto incluye la automatización de **pruebas UI** sobre el sitio **SwagLabs (SauceDemo)** y **pruebas de API** sobre la API pública **ReqRes**, utilizando **Python** y **Pytest**.

Se aplican buenas prácticas de automatización, como **Page Object Model (POM)**, uso de **fixtures**, y generación de **reportes HTML**.

## 📌 Propósito del proyecto

El objetivo de este proyecto es:

* Practicar y demostrar conocimientos en **automatización de pruebas UI con Selenium**.
* Implementar **pruebas automatizadas de API** usando `requests` y Pytest.
* Aplicar **buenas prácticas de diseño**, como **Page Object Model (POM)** para UI.
* Centralizar configuraciones y utilidades mediante `conftest.py`.
* Generar **reportes HTML** claros y visuales para el análisis de resultados.

## 🧪 Alcance de las pruebas

### 🔹 Pruebas UI – SwagLabs (SauceDemo)

Sitio: [https://www.saucedemo.com](https://www.saucedemo.com)

Flujos automatizados:

* Login de usuario
* Validación del inventario
* Agregado de productos al carrito
* Reseteo del estado de la aplicación

Las pruebas UI están estructuradas utilizando **Page Object Model (POM)** para mejorar:

* Legibilidad
* Mantenibilidad
* Reutilización de código

### 🔹 Pruebas de API – ReqRes

API utilizada: [https://reqres.in](https://reqres.in)

Endpoints cubiertos:

* Obtener usuario por ID (GET)
* Listar usuarios (GET)
* Crear usuario (POST)
* Eliminar usuario (DELETE)
* Login exitoso (POST)
* Login fallido (POST – caso negativo)

Las pruebas de API validan:

* Códigos de estado HTTP
* Estructura del response
* Datos clave devueltos por la API

⚠️ **Nota importante**: ReqRes actualmente requiere el uso de una **API Key** para acceder a sus endpoints.


## 🛠️ Tecnologías utilizadas

* **Python**
* **Pytest**
* **Selenium WebDriver**
* **Requests** (para API testing)
* **Google Chrome**
* **ChromeDriver**
* **pytest-html** (reportes)


## ⚙️ Instalación y configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/osunamartin/pre-entrega-automation-testing-martin-osuna.git
cd pre-entrega-automation-testing-martin-osuna
```

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv venv
```

* Linux / Mac:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```

### 3️⃣ Instalar dependencias

```bash
pip install selenium pytest requests pytest-html
```

⚠️ Selenium debe ser versión **4.36.0 o superior**.

### 4️⃣ Configurar API Key de ReqRes

Crear una API Key gratuita en:
👉 [https://app.reqres.in](https://app.reqres.in)

Luego agregarla en el fixture correspondiente (por ejemplo, en `conftest.py`):

```python
@pytest.fixture
def api_headers():
    return {
        "x-api-key": "TU_API_KEY_AQUI",
        "Content-Type": "application/json"
    }
```

⚠️ **Usar una apikey válida para este último paso. No se muestra la usada por el autor por motivos de seguridad**.


## ▶️ Ejecución de pruebas

### 🔹 Ejecutar todas las pruebas con Pytest

```bash
pytest -v
```


### 🔹 Ejecutar pruebas con reporte HTML

Para generar un reporte visual:

```bash
pytest --html=reports/report.html --self-contained-html
```

Luego abrir:

```
reports/report.html
```

El reporte incluye:

* Resultado de cada test
* Screenshots automáticos en fallos de UI
* Columna con la URL visitada en tests de Selenium


## 🧩 Estructura del proyecto (resumen parcial)

```
├── tests/
│   ├── test_api_reqres.py
│   ├── test_ui_*.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
├── reports/
│   ├── report.html
│   └── screens/
├── conftest.py
├── pytest.ini
├── README.md
```

## 🧠 Buenas prácticas aplicadas

* Page Object Model (POM)
* Uso de fixtures de Pytest
* Separación de pruebas UI y API
* Casos positivos y negativos
* Reportes automáticos con evidencias

---

## ⚠️ Si bien existe un archivo behave.ini, no se terminó de implementar para este proyecto.

## 👤 Autor

**Martín Osuna**
Proyecto realizado como práctica y entrega académica de automatización de pruebas.
