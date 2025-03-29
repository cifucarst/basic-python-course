import logging

# Crear un logger personalizado
logger = logging.getLogger("SecurityLogger")
logger.setLevel(logging.DEBUG)

# Crear un manejador para escribir en un archivo
file_handler = logging.FileHandler("security.log")
file_handler.setLevel(logging.WARNING)

# Crear un manejador para imprimir en la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Definir un formato para los logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Agregar los manejadores al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Registrar eventos
logger.debug("Mensaje de depuración (debug)")
logger.info("Mensaje de información")
logger.warning("Advertencia: actividad sospechosa detectada")
logger.error("Error en el sistema de autenticación")
logger.critical("Ataque detectado: fuerza bruta en la cuenta admin")