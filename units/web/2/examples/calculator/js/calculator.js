window.addEventListener('load', handleLoad);

function handleLoad() {
    var calculateButton = document.querySelector('#calculate');
    var clearButton = document.querySelector('#clear');
    var minusButton = document.querySelector('#minus');

    calculateButton.addEventListener('click', handleCalculateClick);
    clearButton.addEventListener('click', handleClearClick);
    minusButton.addEventListener('click', handleMinusClick);
}

function handleMinusClick() {
    console.log('Minus button clicked.');

    var operator = document.querySelector('#operator');

    operator.innerText = '-';
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
