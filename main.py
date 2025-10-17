from bot import Bot
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bot is running on @bynude_bot!')

def run_server():
    port = int(os.environ.get('PORT', 8080))  # Use PORT env var (set to 8080)
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    print(f"Listening on port {port} (dummy server for Render)")
    server.serve_forever()

if __name__ == '__main__':
    # Start the bot in a background thread
    bot_thread = threading.Thread(target=lambda: Bot().run(), daemon=True)
    bot_thread.start()
    print("Bot started in background thread")

    # Start dummy HTTP server in the main thread
    run_server()
