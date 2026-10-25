import os
import sys
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 5200
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    local_ip = get_local_ip()
    print(f"=====================================================")
    print(f"🚀 EngMastery AI Local App Server Running!")
    print(f"📱 Trên Máy Tính: http://localhost:{PORT}")
    print(f"📲 Trên Điện Thoại (Cùng Wi-Fi): http://{local_ip}:{PORT}")
    print(f"=====================================================")
    
    server_address = ('0.0.0.0', PORT)
    try:
        httpd = HTTPServer(server_address, CORSRequestHandler)
        httpd.serve_forever()
    except OSError as e:
        # Port might already be in use
        print(f"Server is already running on port {PORT} or port is busy.")
