import socket
from urllib.parse import urlparse

def http_request(host, port=80, path="/"):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    client.send(request.encode())

    response = client.recv(9096).decode()
    print("[RESPUESTA INICIAL]")
    print(response)

    # Buscar redirección
    if "Location:" in response:
        for line in response.split("\r\n"):
            if line.lower().startswith("location:"):
                location = line.split(":", 1)[1].strip()
                print(f"[INFO] Redirigiendo a: {location}")
                
                parsed = urlparse(location)
                new_host = parsed.hostname
                new_port = parsed.port or 80
                new_path = parsed.path or "/"

                # Llamada recursiva para seguir redirección
                return http_request(new_host, new_port, new_path)

    return response

# Ejecutar
http_request("www.google.com")