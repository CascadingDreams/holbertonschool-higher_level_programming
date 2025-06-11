#!/usr/bin/python3

'''Basic simple API module with http.server'''

import http.server
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    '''Creates MyHandler class'''
    def do_GET(self):
        '''handles GET requests'''
        if self.path == '/':
            # Handle homepage
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


if __name__ == "__main__":
    '''starts server'''
    server = http.server.HTTPServer(('localhost', 8000), MyHandler)
    print("Server starting on http://localhost:8000")
    server.serve_forever()
