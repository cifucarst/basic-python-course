import logging

# Configurar logging para escribir en un archivo
logging.basicConfig(filename='registro.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Inicio del programa")
logging.warning("Intento de acceso no autorizado detectado")
logging.error("Fallo en la autenticación del usuario")