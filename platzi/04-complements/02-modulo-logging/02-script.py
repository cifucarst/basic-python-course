import logging

# Configurar el nivel de logging y formato del mensaje
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Diferentes niveles de log
logging.debug("Este es un mensaje de depuración")
logging.info("Esto es un mensaje informativo")
logging.warning("¡Advertencia! Algo podría salir mal")
logging.error("Error detectado en el sistema")
logging.critical("¡Falla crítica! El sistema puede colapsar")