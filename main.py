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

    def do_HEAD(self):  # Handle HEAD requests for Render health checks
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

def run_server():
    port = int(os.environ.get('PORT', 8080))  # Use PORT env var (set to 8080)
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    print(f"Listening on port {port} (dummy server for Render)")
    server.serve_forever()

def run_bot():
    # Create a new event loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        # Initialize and run the bot
        bot = Bot()
        loop.run_until_complete(bot.run())  # Run async run() method
    finally:
        loop.close()

if __name__ == '__main__':
    # Start the bot in a background thread with its own event loop
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    print("Bot started in background thread")

    # Start dummy HTTP server in the main thread
    run_server()
