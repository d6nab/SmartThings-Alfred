import httplib
import urllib
import urlparse
import BaseHTTPServer, SimpleHTTPServer
import json

HOST_NAME = 'localhost'
PORT_NUMBER = 2222

CLIENT_ID = 'myclient'
CLIENT_SECRET = 'mysecret'


class StoppableHttpServer(BaseHTTPServer.HTTPServer):
    def serve_forever(self):
        self.stop = False
        while not self.stop:
            self.handle_request()


class StoppableHttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print "Processing %s" % self.path
        if "/success" in self.path:
            print "Stopping embedded HTTP server"
            self.send_response(200)
            self.end_headers()
            self.wfile.write("<html><head><title>Authentication success!</title></head>")
            self.wfile.write("<body>Authentication was successful.</body></html>")
            self.server.stop = True
        elif "/oauth/callback" in self.path:
            print "Received OAuth callback"
            parsed_path = urlparse.urlparse(self.path)
            try:
                params = dict([p.split('=') for p in parsed_path[4].split('&')])
            except:
                params = {}
            oauth_params = {
                'grant_type': 'authorization_code',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'scope': 'app',
                'redirect_uri': 'http://localhost:2222/oauth/callback',
                'code': params['code']
            }
            oauth_headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
            conn = httplib.HTTPConnection("localhost", 8080)
            conn.request("POST", "/data-management/oauth/token",
                         urllib.urlencode(oauth_params), oauth_headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()

            jsonData = json.loads(data)

            token = jsonData["access_token"]
            authHeader = open("token.txt", "w")
            authHeader.write(token)
            authHeader.close()

            # Redirect so we can shut down the HTTP server
            self.send_response(301)
            self.send_header("Location", "http://localhost:2222/success")
            self.end_headers()
        else:
            print "%s not found" % self.path
            self.send_response(404)


def start_server():
    httpd = StoppableHttpServer((HOST_NAME, PORT_NUMBER), StoppableHttpRequestHandler)
    print "Starting embedded HTTP server"
    httpd.serve_forever()
