from http.server import HTTPServer, BaseHTTPRequestHandler

class MyApp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello! My DevOps project is running.")

server = HTTPServer(("0.0.0.0", 8000), MyApp)
server.serve_forever()
