import httplib, urllib, urlparse
import time
import BaseHTTPServer

HOST_NAME = 'localhost'
PORT_NUMBER = 2222

CLIENT_ID = 'myclient'
CLIENT_SECRET = 'mysecret'

class OAuthHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        parsed_path = urlparse.urlparse(s.path)
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
        print urllib.urlencode(oauth_params)
        conn = httplib.HTTPConnection("localhost", 8080)
        conn.request("POST", "/data-management/oauth/token", urllib.urlencode(oauth_params), oauth_headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        print data
        conn.close()

        s.send_response(200)
        s.send_header("Content-Type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>OAuth Access Token</title></head>")
        s.wfile.write("<body><p>OAuth Access Token: %s" % data)
        s.wfile.write("</body></html>")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), OAuthHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOSTNAME, PORT_NUMBER)
