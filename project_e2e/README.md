Prueba funcional automatizada (Prueba E2E) en la página https://www.saucedemo.com/
Este proyecto contiene una prueba funcional automatizada (Prueba E2E) de un flujo de compra en la página https://www.saucedemo.com/. 
La prueba incluye las siguientes acciones:

Autenticarse con el usuario: standard_user y password: secret_sauce
Agregar dos productos al carrito
Visualizar el carrito
Completar el formulario de compra
Finalizar la compra hasta la confirmación: “THANK YOU FOR YOUR ORDER”
Requisitos previos
Antes de ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

Python 3.0
pip
Instalación
Clona el repositorio en tu máquina local:
bash
Copy code
git clone git@github.com:ktroch/project_e2e.git
Navega al directorio raíz del proyecto:
bash
Copy code
cd prueba-e2e-saucedemo
Instala las dependencias utilizando el archivo requirements.txt:
Copy code
pip install -r requirements.txt
Ejecución de las pruebas
Para ejecutar las pruebas, navega al directorio raíz del proyecto y ejecuta el siguiente comando:

css
Copy code
pytest --html=report.html
Este comando ejecutará todas las pruebas en el proyecto y generará un reporte HTML en el archivo report.html.

Estructura del proyecto
tests/: Este directorio contiene todos los archivos de prueba.
pages/: Este directorio contiene los objetos de página para las diferentes páginas de la aplicación.
config.py: Este archivo contiene las variables de configuración para el proyecto.
constants.py: Este archivo contiene todas las constantes utilizadas en el proyecto.
logger.py: Este archivo contiene la configuración del logger utilizado en el proyecto.
report.html: Este archivo contiene el reporte generado por pytest-html.
requirements.txt: Este archivo contiene todas las dependencias necesarias para ejecutar el proyecto.
Contribuciones
Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.
