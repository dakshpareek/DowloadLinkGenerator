import CGIHTTPServer
import BaseHTTPServer

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi"]

PORT = 8888

httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
print("serving at localhost:", PORT)
httpd.serve_forever()