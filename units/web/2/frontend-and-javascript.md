Frontend and Javascript Basics
==============================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/web/1/web-basics-and-http.md) | [Next →]()

This is a tutorial using HTML, CSS & JavaScript to build a Calculator with an objective to let the beginner understand what HTML, CSS and JavaScript are and how we use them to built the Frontend of the Web. 

If you want a complete step-by-step guide using [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS) and [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics) from the basics then you may start with [this tutorial](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web). The [MDN](https://developer.mozilla.org/en-US/) guys have done a really good job on building a complete guide for Web beginners.

So far we've focussed more on theoritical aspects on our previous lessons, but in this session we'll dive directly into the code and you can read about them in detail afterwards following the links I've posted below.

## Hello Web!
Let's get started with a "Hello World" example for the Web.

### HTML
HTML is a markup language which is used to tell your browser how to display and render the webpages.

A "hello world" for html couldn't be any more simpler than this html page.

Create a new directory for our tutorial and create a file named `index.html` with the following code.
```html
<html>
  <head>
    <title>Hello Web!</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```
Open this page in the browser and you should see a very basic Web Page that you've just created.

Alternatively, `cd` to this directory and run the python server to start serving this whole directory.
```
$ python -m SimpleHTTPServer 8000
```
For python 3 you can do this instead:
```
$ python3 -m http.server 8000
``` 
Now just navigate to [http://localhost:8000](http://localhost:8000) and you should see your first web page.

### CSS
Just like HTML, CSS isn't a programming language either; it's a webpage styling language. CSS stands for *Cascading Style Sheets*.

Now let's add some css styles the page that we've just created to understand how it's used. Create a sub-directory `css` with a file `style.css`. The file `css/style.css` should have the following code:

```css
body {
    margin: 0;
    padding: 0;
    background: #eaeaea;
}

h1 {
    margin-top: 20px;
    margin-bottom: 20px;
    text-align: center;
    font-weight: 500;
    color: #666;
    font-size: 30px;
}
```

Then add this line with under the `<head>` tag of our `index.html` file.
```html
<head>
  <title>Hello Web!</title>
  <link href="css/style.css" rel="stylesheet" />
</head>
```
This will add a link to the `css/style.css` css file that we've just created. Refresh your browser and you should see that our page has some formatting. This is what css is all about: formatting, styling and the design that you could see in web pages.

Now let's add some more content to our `index.html` page in the `<body>` section.
```html
<body>
  <h1>Hello World</h1>
  <p>I'm learning to Web Development.</p>
</body>
```

Add some additional styles in our `style.css` file for our new `<p>` tag as well.
```css
p {
    text-align: center;
    font-size: 15px;
    color: #999;
}
```
Refresh the page you should see the updated content and styles are reflected.


## Read More?
If you want to dive really deep into the world of frontend, first go through these links one-by-one. They cover almost everything you need to know about the getting started with modern Web Development from the "basics" to advanced stuff slowly and gradually.
1. https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web
2. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
3. https://github.com/getify/You-Dont-Know-JS

