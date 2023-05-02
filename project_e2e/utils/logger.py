import logging
import os
from datetime import datetime

# Configuración del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Creación de la carpeta logs si no existe
if not os.path.exists('logs'):
    os.makedirs('logs')

# Definición del nombre del archivo de registro
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f'logs/test_log_{now}.log'

# Configuración del manejador de archivo para guardar los registros
file_handler = logging.FileHandler(log_filename)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Configuración del manejador de consola para mostrar los registros
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

# Agregamos ambos manejadores al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
