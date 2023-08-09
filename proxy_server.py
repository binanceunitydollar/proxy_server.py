from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import random
import time

ip_addresses = ["199.70.1.111", "199.70.1.112", "199.70.1.113","199.70.1.114"]
port = 8080
interval_seconds = 30

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = random.choice(ip_addresses)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f"Using proxy IP: {ip}".encode())

def run_proxy_server(server_class=HTTPServer, handler_class=ProxyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting proxy server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        run_proxy_server(port=port)
    except KeyboardInterrupt:
        print("Proxy server stopped")
