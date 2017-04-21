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
  <p>I'm learning Web Development.</p>
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

### JavaScript
Now, unlike HTML & CSS JavaScript is a programming language that browsers support out of the box. It let's you implement the logic into your web page, or even let you transform your static web page into a web based application. 

Although, javascript initially was created just do make html pages a little dynamic. Now the use of javascript has changed as web has evolved. Today, JavaScript is one of the [most popular programming languages](https://stackoverflow.com/insights/survey/2017#most-popular-technologies) of the world as of 2017 that is used to build simple to complex web applications.

Now let's see how we can add some logic to our page using JavaScript.

Create a file `hello.js` under `js` directory in our root folder.
Our directory structure would look like this now:

```
css/
  style.css
js/
  hello.js
index.html
```

Save the `js/hello.js` file with the following code.
```javascript
window.addEventListener('load', handleLoad);

function handleLoad() {
    document.querySelector('p').innerHTML = "I'm learning Web Development with HTML, CSS and JavaScript.";
}
```

Now we need to load this script in our html page too. For this we'll add a `<script>` tag inside our `<body>` tag like this:

```html
<body>
  <h1>Hello World</h1>
  <p>I'm learning Web Development.</p>

  <!-- Load our JavaScript file -->
  <script src="js/hello.js"></script>
</body>
```

Refresh the page and you'll notice what is changed. Did you notice how we've changed the contents of the `<p>` dynamically using JavaScript?

Great! Let's do one additional improvement here. Let's make the content change noticable by delaying the change after few seconds.

Refactor our `hello.js` file to something like this:

```javascript
window.addEventListener('load', handleLoad);

function handleLoad() {
    // This will invoke the changeContent function after 3 seconds.
    setTimeout(changeContent, 3000);
}

function changeContent() {
    // This will change the content of the <p> tag.
    document.querySelector('p').innerHTML = "I'm learning Web Development with HTML, CSS and JavaScript.";
}
```

Now refresh the page, wait for 3 seconds and you'll see what the above code just did. Pretty neat right? Awesome. 

This was a very simple Hello World example for Web Development (Frontend).

Check the full source code for this example [here](examples/hello-world).

## Building a Calculator
Now let's try an example that involves a litte bit more logic and JavaScript. Here we'll build a very simple calculator application.

### Basic Calculator
First create a new directory with files `index.html`, `css/style.css` and `js/calculator.js`. Our directory structure should look like this:
```
css/
  style.css
js/
  calculator.js
index.html
```

Now add the following code in each file:

**index.html**:
```html
<html>
<head>
  <title>Calculator</title>
  <link href="css/style.css" rel="stylesheet" />
</head>
<body>
  <div id="calculator">
    <h1>Calculator</h1>

    <div class="input-group">
      <div>
        <input id="input1" type="text" /> +
        <input id="input2" type="text" />
      </div>
      <div>
        <span id="output"></span>
      </div>
    </div>

    <div class="button-group">
      <button id="calculate">Calculate</button>
    </div>
  </div>
  <script src="js/calculator.js"></script>
</body>
</html>
```

**css/style.css**:
```css
body {
    margin: 0;
    padding: 0;
    background: #eaeaea;
}

body * {
    font-size: 16px;
}

h1 {
    margin-top: 20px;
    margin-bottom: 20px;
    text-align: center;
    font-weight: 500;
    color: #666;
    font-size: 30px;
}

#calculator {
    display: table;
    margin: 20px auto;
}

.input-group {
    margin-bottom: 15px;
}
.input-group input {
    width: 100px;
    padding: 5px;
    margin: 5px;
    font-size: 20px;
    text-align: right;
}

#output {
    font-size: 20px;
    display: inline-block;
    height: 24px;
    border: 1px solid #999;
    margin: 5px;
    padding: 5px;
    width: calc(100% - 24px);
    text-align: right;
}

.button-group {
    padding: 5px;
}
```

**js/calculator.js**:
```javascript
window.addEventListener('load', handleLoad);

function handleLoad() {
    var calculateButton = document.querySelector('#calculate');

    calculateButton.addEventListener('click', handleCalculateClick);
}

function handleCalculateClick() {
    console.log('Calculate Button Clicked.');

    // Get the input & result elements
    var input1 = document.querySelector('#input1');
    var input2 = document.querySelector('#input2');
    var output = document.querySelector('#output');

    // Get the values.
    var value1 = Number(input1.value);
    var value2 = Number(input2.value);

    // Just add those two values.
    var result = value1 + value2;

    // Update the output element's content.
    output.innerHTML = result;
}
```

Now open the `index.html` file in your browser. You should see the calculator application running.

### Add clear feature
Let's add a new `Clear` button in our application that would clear the fields.

Firstly, we'll need to add one more button in our html.

```html
    ...
    <div class="button-group">
      <button id="calculate">Calculate</button>
      <button id="clear">Clear</button>
    </div>
    ...
```

Now that we have a button. Let's create a new event handler for this button in our javascript code to make it functioning.

Add this new function that will handle the `click` event for our clear button.
```javascript
function handleClearClick() {
    console.log('Clear Button Clicked.');

    // Get the input & result elements.
    var input1 = document.querySelector('#input1');
    var input2 = document.querySelector('#input2');
    var output = document.querySelector('#output');

    // Clear the fields and output.
    input1.value = '';
    input2.value = '';
    output.innerHTML = '';
}
```
We have an event handler function now. But we need to register it for the `click` event first. For this we'll make some changes in our `handleLoad` function.
```javascript
function handleLoad() {
    var calculateButton = document.querySelector('#calculate');
    var clearButton = document.querySelector('#clear');

    calculateButton.addEventListener('click', handleCalculateClick);
    clearButton.addEventListener('click', handleClearClick);
}
```
Now refresh your browser can you can see the `Clear` button is fully functional.

Well Done! You've just create a very simple web application.
Check the full source code for this calculator [here](examples/calculator).

## Exercises
1. Add buttons `+`, `-`, `*`, & `/`. 
2. On clicking these buttons the operator for the calcuation should change and the result should now be calculated depending upon which button is pressed.
3. Input validation: Display invalid input message to the user if the user supplies non-number inputs.

## Read More?
If you want to dive really deep into the world of frontend, first go through these links one-by-one. They cover almost everything you need to know about the getting started with modern Web Development from the "basics" to advanced stuff slowly and gradually.
1. https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web
2. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
3. https://github.com/getify/You-Dont-Know-JS

