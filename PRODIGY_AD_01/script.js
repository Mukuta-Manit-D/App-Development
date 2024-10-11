// JavaScript Code for Calculator Logic
function performCalculation() {
    // Get the input values and operation type
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const operation = document.getElementById("operation").value;
    const resultElement = document.getElementById("result");
    const errorElement = document.getElementById("error");

    let result = 0;

    // Clear previous results and errors
    resultElement.innerHTML = "";
    errorElement.innerHTML = "";

    // Check if numbers are valid
    if (isNaN(num1) || isNaN(num2)) {
        errorElement.innerHTML = "Please enter valid numbers!";
        return;
    }

    // Perform the selected operation
    switch (operation) {
        case "add":
            result = num1 + num2;
            break;
        case "subtract":
            result = num1 - num2;
            break;
        case "multiply":
            result = num1 * num2;
            break;
        case "divide":
            if (num2 === 0) {
                errorElement.innerHTML = "Error! Division by zero is not allowed.";
                return;
            }
            result = num1 / num2;
            break;
        default:
            errorElement.innerHTML = "Invalid operation selected!";
            return;
    }

    // Display the result
    resultElement.innerHTML = `Result: ${result}`;
}
   