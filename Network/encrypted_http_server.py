#!/usr/bin/python3  # Specifies the interpreter to use for running the script

from http.server import HTTPServer, BaseHTTPRequestHandler  # Import modules for handling HTTP requests
import ssl  # Import SSL module for HTTPS encryption

# Define a custom request handler by extending BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # Handle GET requests
        self.send_response(200)  # Send HTTP status 200 (OK)
        self.end_headers()  # End HTTP headers
        self.wfile.write(b"Hello, world!")  # Send response body as bytes

# Create an HTTP server that listens on localhost at port 8080
https_server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)

# Create an SSL context for securing the server with TLS
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")  # Load SSL certificate and private key

# Secure the server socket with SSL/TLS encryption
https_server.socket = context.wrap_socket(https_server.socket, server_side=True)  # Fixed variable name typo

# Start the HTTPS server to handle incoming requests indefinitely
https_server.serve_forever()



'''
──(root㉿kali)-[/home/kali/python/network]
└─# python e_https_server.py 
Enter PEM pass phrase:
127.0.0.1 - - [20/Feb/2025 23:42:38] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [20/Feb/2025 23:42:39] "GET /favicon.ico HTTP/1.1" 200 -
'''