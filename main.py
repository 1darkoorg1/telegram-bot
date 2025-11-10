import threading, http.server, socketserver

def run_http_server():
    port = int(os.getenv("PORT", "8000"))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_http_server, daemon=True).start()
