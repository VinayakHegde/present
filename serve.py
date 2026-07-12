#!/usr/bin/env python3
"""Static server with SPA fallback: real files are served as-is,
any other path (extensionless routes like /system-design/stock-price-alerts)
falls back to index.html so the app shell can resolve it client-side."""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_head(self):
        path = self.translate_path(self.path.split("?")[0].split("#")[0])
        # Only real files are served as-is; directories (e.g. /behavioural) are
        # SPA routes and must load the shell, not the directory index.
        if not os.path.isfile(path):
            self.path = "/index.html"
        return super().send_head()


if __name__ == "__main__":
    print(f"Serving {ROOT} at http://localhost:{PORT}")
    ThreadingHTTPServer(("", PORT), Handler).serve_forever()
