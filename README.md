# Proyecto de Automatización con Selenium – SwagLabs

Este proyecto automatiza pruebas básicas sobre el sitio [SauceDemo](https://www.saucedemo.com) utilizando **Selenium** en Python.  
El flujo incluye login, validación de inventario, agregar productos al carrito y resetear el estado de la aplicación.

## 📌 Propósito del proyecto
El objetivo es:
- Practicar y demostrar conocimientos en **automatización de pruebas con Selenium**.
- Aplicar **buenas prácticas** de organización del código, separando funciones auxiliares y scripts de pruebas.
- Ejecutar un flujo completo de usuario en la aplicación SwagLabs.


## 🛠️ Tecnologías utilizadas
- **Python**
- **Selenium WebDriver**
- **Google Chrome** (navegador)
- **ChromeDriver** (driver de comunicación entre Selenium y Chrome)

## ⚙️ Instalación de dependencias

1. Clonar este repositorio:

   git clone https://github.com/osunamartin/pre-entrega-automation-testing-martin-osuna.git
   cd 'pre-entrega-automation-testing-martin-osuna'

2. Crear y activar un entorno virtual:
   
   python -m venv venv
   source venv/bin/activate     # Linux / Mac
   venv\Scripts\activate        # Windows

3. Instalar dependencias necesarias:

   pip install selenium (debe ser la versión 4.36.0 o superior)

4. (Scripts probados en Google Chrome) Verificar que Google Chrome esté instalado y asegurarse de tener la versión de ChromeDriver correspondiente a la versión del navegador.

5. Ejecutar scripts de pruebas:

  (Ejecución directa): python test_swaglabs.py 
  (Con Pytest luego de haberlo instalado bajo el comando pip install pytest):  pytest -v


## ❌ Errores conocidos:

   Al momento de ejecutar el último paso (reinicio de la página a su estado original) algunas veces aparece una alerta seguridad de contraseña, lo que hace que este paso no llegue a ejecutarse.
