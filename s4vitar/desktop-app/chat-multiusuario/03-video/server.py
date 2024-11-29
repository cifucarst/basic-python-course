#!/usr/bin/env python3

import socket
import threading
import ssl

def client_thread(client_socket, clients, usernames):
    # Receive and decode the username from the client
    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username

    print(f"\n[+] User {username} has connected to the chat")

    # Notify all clients except the new one that a new user has joined
    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] User {username} has joined the chat\n\n".encode())

    while True:
        try:
            # Receive and decode messages from the client
            message = client_socket.recv(1024).decode()
            
            # Break the loop if no message is received (client disconnected)
            if not message:
                break

            # If the client requests the list of users, send it
            if message == "!usuarios":
                client_socket.sendall(f"\n[+] List of available users: {', '.join(usernames.values())}\n\n".encode())
                continue

            # Send the received message to all other clients
            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{message}\n".encode())

        except:
            break

    # Close the client socket and remove the client from the list and username dictionary
    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]

def server_program():
    host = 'localhost'
    port = 12345

    # Create a socket and set options to allow address reuse
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    
    # Wrap the socket in SSL for secure communication
    server_socket = ssl.wrap_socket(server_socket, keyfile="server-key.key", certfile="server-cert.pem", server_side=True)
    server_socket.listen()

    print(f"\n[+] The server is listening for incoming connections...")

    clients = []
    usernames = {}

    while True:
        # Accept new client connections
        client_socket, address = server_socket.accept()
        clients.append(client_socket)

        print(f"\n[+] A new client has connected: {address}")

        # Start a new thread to handle the connected client
        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()

    # Close the server socket
    server_socket.close()

if __name__ == '__main__':
    server_program()


"""
At this final stage, we will add the finishing touches to our multi-user chat, 
focusing on the security and privacy of conversations. We will use the SSL library 
and tools like OpenSSL to implement robust encryption.

We will learn how to integrate these technologies into our chat to ensure that 
communications between users are secure and private. This session is crucial to 
understanding the importance of encryption in messaging applications and how to 
apply it effectively in real projects.

Below are the commands used in the class:

1. Generate a new RSA private key, encrypted with AES-256:
"""
# openssl genpkey -algorithm RSA -out server-key.key -aes256

"""
This command generates a new RSA private key. The `-algorithm RSA` option specifies 
the use of the RSA algorithm. `-out server-key.key` indicates that the generated key 
will be saved in a file named `server-key.key`. The `-aes256` option means that the 
private key will be encrypted using the AES-256 algorithm, adding a layer of security 
by requiring a password to access the key.

2. Create a new Certificate Signing Request (CSR) using the RSA private key:

"""

# openssl req -new -key server-key.key -out server.csr

"""
This command creates a new Certificate Signing Request (CSR) using the RSA private 
key you generated. `-new` indicates a new request, `-key server-key.key` specifies 
that the private key stored in `server-key.key` will be used, and `-out server.csr` 
saves the generated CSR in a file named `server.csr`. The CSR is necessary to request 
a digital certificate from a Certificate Authority (CA).

3. Generate a self-signed certificate based on the CSR:

"""

# openssl x509 -req -days 365 -in server.csr -signkey server-key.key -out server-cert.pem

"""
This command generates a self-signed certificate based on the CSR. `-req` indicates 
processing a CSR, `-days 365` sets the certificate's validity to one year, `-in 
server.csr` specifies the input CSR, `-signkey server-key.key` uses the same private 
key to sign the certificate, and `-out server-cert.pem` saves the generated certificate 
in a file named `server-cert.pem`.

4. Remove the password from the RSA private key:

"""

# openssl rsa -in server-key.key -out server-key.key

"""
This command removes the password from an AES-256 encrypted RSA private key. 
`-in server-key.key` specifies the input file of the encrypted private key, and 
`-out server-key.key` indicates that the unencrypted private key will be saved in 
the same file, overwriting the encrypted version. This step is often done to 
simplify automation in environments where manually entering a password is impractical. 
However, be aware that removing the password makes the private key more vulnerable to 
unauthorized access.
"""