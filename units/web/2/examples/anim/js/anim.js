window.addEventListener('load', handleLoad);

var x = 0;
var y = 0;
var dX = 1;
var dY = 1;

function handleLoad() {
    animate();
}

function animate() {
    var duration = 5;

    setInterval(update, duration);
}

function update() {
    var container = document.querySelector('#container');
    var box = document.querySelector('#box');
    var boxRight = x + box.offsetWidth;
    var boxBottom = y + box.offsetHeight;
    var delta = 2;

    if (boxRight >= container.clientWidth) {
        dX = -1;
    } else if (x <= 0) {
        dX = +1;
    }

    if (boxBottom >= container.clientHeight) {
        dY = -1;
    } else if (y <= 0) {
        dY = +1;
    }

    x = x + dX * delta;
    y = y + dY * delta;
    
    // Update the box CSS.
    box.style.left = x + 'px';
    box.style.top = y + 'px';
}

