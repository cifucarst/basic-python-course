import socket
import ssl
import sys
from urllib.parse import urlparse

def analizar_cabeceras(cabeceras):
    print("\n[+] Análisis de cabeceras HTTP:")
    for clave, valor in cabeceras.items():
        print(f"  {clave}: {valor}")

    # Ejemplo básico de verificación
    server = cabeceras.get("Server", "").lower()
    x_powered = cabeceras.get("X-Powered-By", "").lower()

    if "apache" in server:
        print("  [!] El servidor usa Apache, puede ser vulnerable si no está actualizado.")
    if "php" in x_powered:
        print("  [!] El servidor usa PHP, busca versiones obsoletas.")
    if "nginx" in server:
        print("  [i] Servidor nginx detectado.")
    if not cabeceras.get("Content-Security-Policy"):
        print("  [!] Falta la cabecera Content-Security-Policy (CSP).")

def parsear_respuesta(respuesta):
    partes = respuesta.split(b"\r\n\r\n", 1)
    cabecera_bruta = partes[0].decode("iso-8859-1")
    cuerpo = partes[1] if len(partes) > 1 else b""

    lineas = cabecera_bruta.split("\r\n")
    status_line = lineas[0]
    cabeceras = {}
    for linea in lineas[1:]:
        if ": " in linea:
            clave, valor = linea.split(": ", 1)
            cabeceras[clave] = valor

    return status_line, cabeceras, cuerpo

def realizar_peticion(url, max_redirecciones=5):
    for intento in range(max_redirecciones):
        print(f"\n[*] Intento #{intento + 1}: {url}")
        parsed_url = urlparse(url)
        host = parsed_url.hostname
        puerto = parsed_url.port or (443 if parsed_url.scheme == "https" else 80)
        ruta = parsed_url.path or "/"

        if parsed_url.query:
            ruta += "?" + parsed_url.query

        try:
            sock = socket.create_connection((host, puerto), timeout=10)

            if parsed_url.scheme == "https":
                context = ssl.create_default_context()
                sock = context.wrap_socket(sock, server_hostname=host)

            peticion = f"GET {ruta} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: HackScanner/1.0\r\nConnection: close\r\n\r\n"
            sock.send(peticion.encode())

            respuesta = b""
            while True:
                datos = sock.recv(4096)
                if not datos:
                    break
                respuesta += datos
            sock.close()

            status, cabeceras, cuerpo = parsear_respuesta(respuesta)

            print(f"[+] Estado HTTP: {status}")
            analizar_cabeceras(cabeceras)

            # Guardar HTML
            with open("respuesta.html", "wb") as archivo:
                archivo.write(cuerpo)
                print("[+] HTML guardado en 'respuesta.html'.")

            if "Location" in cabeceras and status.startswith("3"):
                url = cabeceras["Location"]
                print(f"[→] Redirigiendo a: {url}")
                continue

            break  # si no hay redirección

        except Exception as e:
            print(f"[!] Error en la petición: {e}")
            break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python escaner_web.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    realizar_peticion(url)