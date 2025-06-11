#!/usr/bin/python3

'''Basic simple API module with http.server'''

import http.server
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    '''Creates MyHandler class'''
    def do_GET(self):
        '''handles GET requests'''
        # Step 1: Tell them "OK, I got your request"
        self.send_response(200)
        # Step 2: Tell them what kind of answer I'm giving
        self.send_header('Content-type', 'text/plain')
        # Step 3: Say "I'm done with the info, here comes the actual answer"
        self.end_headers()
        # Step 4: Give them the actual answer
        self.wfile.write(b'Hello, this is a simple API!')


if __name__ == "__main__":
    '''starts server'''
    server = http.server.HTTPServer(('localhost', 8000), MyHandler)
    print("Server starting on http://localhost:8000")
    server.serve_forever()
