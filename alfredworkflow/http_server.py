import httplib
import urllib
import urlparse
import BaseHTTPServer, SimpleHTTPServer
import json
from settings import SERVER_PORT, PROTOCOL, HOSTNAME, PORT, CLIENT_ID, CLIENT_SECRET


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
            try:
                self.wfile.write(open("login_success.html").read())
            except IOError:
                self.wfile.write("<html><head><title>Authentication success!</title></head>")
                self.wfile.write("<body>Authentication was successful. Remember to run <b>st_update</b> in Alfred.</body></html>")
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
                'redirect_uri': "http://localhost:{port}/oauth/callback".format(port=SERVER_PORT),
                'code': params['code']
            }
            oauth_headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
            connection = httplib.HTTPSConnection if PROTOCOL == "https" else httplib.HTTPConnection
            conn = connection(HOSTNAME, PORT)
            conn.request("POST", "/oauth/token",
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
            self.send_header("Location", "http://localhost:{port}/success".format(port=SERVER_PORT))
            self.end_headers()
        else:
            print "%s not found" % self.path
            self.send_response(404)


def start():
    httpd = StoppableHttpServer(("localhost", SERVER_PORT), StoppableHttpRequestHandler)
    print "Starting embedded HTTP server"
    httpd.serve_forever()

def stop():
    try:
        conn = httplib.HTTPConnection("localhost", SERVER_PORT)
        conn.request("GET", "/success")
        response = conn.getresponse()
        response.read()
        conn.close()
    except Exception, err:
        pass
