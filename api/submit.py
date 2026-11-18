from http.server import BaseHTTPRequestHandler
import urllib.request
import urllib.error
import json

AWS_URL = "https://w3obh27tnh.execute-api.ap-south-1.amazonaws.com/submit"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        req = urllib.request.Request(
            AWS_URL,
            data=post_data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=20) as response:
                status_code = response.getcode()
                resp_body = response.read()
        except urllib.error.HTTPError as e:
            status_code = e.code
            resp_body = e.read()
        except Exception as e:
            status_code = 500
            resp_body = json.dumps({"error": str(e)}).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(resp_body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
