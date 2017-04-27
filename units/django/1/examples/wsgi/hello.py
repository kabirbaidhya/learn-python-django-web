from wsgiref.simple_server import make_server


def application(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)

    return [b'Hello World']

# Instantiate the server
PORT = 8051
httpd = make_server('localhost', PORT, application)

print("Server is listening on port", PORT)
# Serve the HTTP requests
httpd.serve_forever()
