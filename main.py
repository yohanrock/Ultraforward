from bot import Bot
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bot is running!')

def run_server():
    port = int(os.environ.get('PORT', 8080))  # Use PORT env var, default to 8080
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    print(f"Listening on port {port}")
    server.serve_forever()

if __name__ == '__main__':
    # Start the bot
    app = Bot()
    app.run()

    # Start dummy HTTP server in a background thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Keep main thread alive
    server_thread.join()
