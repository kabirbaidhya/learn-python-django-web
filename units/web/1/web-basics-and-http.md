Web Basics and HTTP
===================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [Slides](https://speakerdeck.com/kabirbaidhya/python-web-basics-and-http) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/database/8/classes-and-objects.md) | [Next →]()

This is a short introduction of the Web, the basics and the concepts about Web Development, Web Application Architecture and the HTTP.

## Web
The World Wide Web (WWW) is a universe of interconnected network of information available via internet and which are accessible via the HTTP protocol.

Information and resources are generally interlinked with each other across networks as hypertext documents or hypermedia.

Today, the Web is not only limited to the hypertext documents and Web Pages but also includes the growing Cloud based applications and the mobile applications that are backed by Web services and applications on the cloud that are made possible due to web.

The HTTP protocol and the internet are the ones that made possible the Web we have today.

## HTTP
 * HTTP(Hypertext Transfer Protocol) is an application layer protocol.
 * Request-Response Protocol
 * Client Sends the HTTP request requesting the resources
 * Server receives the request and responds with the resources

For instance:
An http request would look this:
```
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost
User-Agent: HTTPie/0.9.2
```

And on receiving this request the server could respond with the following response:
```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html
Date: Sat, 08 Apr 2017 00:06:03 GMT
ETag: W/"583bce74-264"
Last-Modified: Mon, 28 Nov 2016 06:28:04 GMT
Server: nginx/1.10.0 (Ubuntu)

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```
### HTTP Request
The end which initiate a request to the server is the HTTP client.

HTTP Request may contain the following things:
    * URIs (Uniform Resource Identifiers)
    * Methods/Verbs
    * Headers
    * Payload/Body

#### URIs(Uniform Resource Identifiers)
URIs are the ones that actually identify a resource on a remote server.

URLs contain a the protocol, hostname followed by the path of the resource on the host at which the resource could be accessible.
```
protocol://hostname/path
```

For instance:
```
https://example.com/users/52/documents/xyz.pdf
```
This could be an example of URL. Here, the protocol used is `https`, hostname is `example.com` and the path to the resource is `/users/52/documents/xyz.pdf`.

##### Query Strings
The URIs could also contain query strings. You probably have seen some thing like `?q=this+was+just+a+test&name=Foo` gets appended to some website url when you press some button like Search. This is the query string which might also come in the URI.

Consider this url:
```
https://example.com/search?q=test&foo=bar
```

Here the part of the url followed by `?` is the query string which is `q=test&foo=bar`. Actually, query string includes some key value pairs that the client sends to server in urlencoded form via the urls.

#### HTTP Methods (Verbs)
The HTTP method should generally differentiate the type of the request on any resource.

The most common HTTP methods used in web applications today are:

1. GET
2. POST
3. PUT
4. PATCH
4. DELETE

#### Request Headers
The request headers will contain meta information about the request.
Request headers look like this:
```
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost
User-Agent: HTTPie/0.9.2
```

#### Request payload/data
HTTP `POST`, `PUT`, `PATCH` requests do need to send data or payload along in request. Consider the case when you are submitting a form to the server. Generally you would just submit the form as a `POST` request. In these cases the form's data is sent along with the request as a payload.

However, in other request methods, payload aren't necessary and are omitted.

## Client
A slient in the Web usually means the software or a program which initiate the HTTP request. Generally these are: Browsers, Mobile Apps, Scripts, Web scrapers, automated scripts or even CLI tools if they rely on HTTP based services.

## Server
In web, a server actually means the http server which is responding to the client's http requests. These could be Nginx Server, Apache HTTP Server, or any http servers made in any language like Python, NodeJs etc as long as they listen on certain port and respond to http requests.

## Testing everything
We'll test how everything works with the http protocol and the web using python's simple http server and a lightweight command line http client tool `httpie`.

## Web Application Architecture
A typical web application could be broken down into 3-tiers:

1. UI (Frontend)
2. Logic (Backend)
3. Data tier (Database)

### UI tier
The UI (User Interface) is the front end of the application which the end user actually interacts with. For the web applications, we use technologies like HTML, CSS, JavaScript and multimedia to develop the UI. But generally this could be anything even mobile apps or CLI applications that communicate with backend Web services or Web APIs.

When we talk about Frontend or Frontend Development we actually talk about developing this layer of the application.

The UI tier (or the frontend) talks with the Logic tier (backend) using the HTTP protocol.

### Logic tier
The UI tier (or the frontend) cannot directly communicate with the database, it needs a sort of middleman to do this work. This is what the Logic tier does, it communicates with the Data tier and also holds the main application logic. Actually, it communicates with the both the tiers and does the performs the business logic. The data might come from and go into the database as per the business logic.

### Data tier
This is actually the layer in the application which holds the application's data. This is mostly the database. It stores the data received from the user (via the middle tier) and also holds the data that are displayed in the UI (via the middle tier).
