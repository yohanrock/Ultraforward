from bot import Bot
import os
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bot is running on @bynude_bot!')

    def do_HEAD(self):  # Handle Render's HEAD health checks
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

def run_server():
    port = int(os.environ.get('PORT', 8080))  # Use PORT env var (set to 8080)
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    print(f"Listening on port {port} (dummy server for Render)")
    server.serve_forever()

if __name__ == '__main__':
    # Start the HTTP server in a background thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    print("HTTP server started in background thread")

    # Run the bot in the main thread
    bot = Bot()
    bot.run()  # Run directly, as Pyrogram manages its own event loop
