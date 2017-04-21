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
