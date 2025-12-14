# Proyecto de Automatización de Pruebas – UI (Selenium) y API (ReqRes)

Este proyecto incluye la automatización de **pruebas UI** sobre el sitio **SwagLabs (SauceDemo)** y **pruebas de API** sobre la API pública **ReqRes**, utilizando **Python** y **Pytest**.

Se aplican buenas prácticas de automatización, como **Page Object Model (POM)**, uso de **fixtures**, y generación de **reportes HTML**.

---

## 📌 Propósito del proyecto

El objetivo de este proyecto es:

* Practicar y demostrar conocimientos en **automatización de pruebas UI con Selenium**.
* Implementar **pruebas automatizadas de API** usando `requests` y Pytest.
* Aplicar **buenas prácticas de diseño**, como **Page Object Model (POM)** para UI.
* Centralizar configuraciones y utilidades mediante `conftest.py`.
* Generar **reportes HTML** claros y visuales para el análisis de resultados.

---

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

---

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

---

## 🛠️ Tecnologías utilizadas

* **Python**
* **Pytest**
* **Selenium WebDriver**
* **Requests** (para API testing)
* **Google Chrome**
* **ChromeDriver**
* **pytest-html** (reportes)

---

## ⚙️ Instalación y configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/osunamartin/pre-entrega-automation-testing-martin-osuna.git
cd pre-entrega-automation-testing-martin-osuna
```

---

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

---

### 3️⃣ Instalar dependencias

```bash
pip install selenium pytest requests pytest-html
```

⚠️ Selenium debe ser versión **4.36.0 o superior**.

---

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

---

## ▶️ Ejecución de pruebas

### 🔹 Ejecutar todas las pruebas con Pytest

```bash
pytest -v
```

---

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

---

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

---

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
