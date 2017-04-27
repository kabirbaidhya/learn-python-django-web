import os
from wsgiref.validate import validator
from wsgiref.simple_server import make_server


def application(env, start_response):
    # Read the html from the file
    html = read_html('html/hello.html')

    # Convert it to byte string
    html = html.encode('ASCII')

    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(html)))
    ]
    start_response('200 OK', headers)

    return [html]


def read_html(filename):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(directory, filename)
    f = open(full_path)
    data = f.read()
    f.close()

    return data

# Instantiate the server
PORT = 8051
httpd = make_server('localhost', PORT, application)

print("Server is listening on port", PORT)
# Serve the HTTP requests
httpd.serve_forever()
