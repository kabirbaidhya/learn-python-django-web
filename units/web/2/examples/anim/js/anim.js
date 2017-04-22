window.addEventListener('load', handleLoad);

var x = 0;
var y = 0;
var dX = 1;
var dY = 1;
var colors = [
    '#923102',
    '#ea66f2',
    '#222',
    '#333',
    '#5f4cd8',
    '#555',
    '#4549e0',
    '#777'
];

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
        changeBgColor(box)
    } else if (x <= 0) {
        dX = +1;
        changeBgColor(box)
    }

    if (boxBottom >= container.clientHeight) {
        dY = -1;
        changeBgColor(box)
    } else if (y <= 0) {
        dY = +1;
        changeBgColor(box)
    }

    x = x + dX * delta;
    y = y + dY * delta;
    
    // Update the box CSS.
    box.style.left = x + 'px';
    box.style.top = y + 'px';
}

function changeBgColor(box) {
    box.style.backgroundColor = randomColor();
}

function randomColor() {
    var index = Math.floor(Math.random() * (colors.length - 1)) + 0;

    return colors[index];
}


