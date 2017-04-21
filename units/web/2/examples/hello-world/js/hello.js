window.addEventListener('load', handleLoad);

function handleLoad() {
    // This will invoke the changeContent function after 3 seconds.
    setTimeout(changeContent, 3000);
}

function changeContent() {
    // This will change the content of the <p> tag.
    document.querySelector('p').innerHTML = "I'm learning Web Development with HTML, CSS and JavaScript.";
}
