document.addEventListener("DOMContentLoaded", function () {
    const randomNumberElement = document.getElementById("randomNumber");
    const binaryRepresentationElement = document.getElementById("binaryRepresentation");

    fetch("/api/players/random-binary")
        .then((response) => response.json())
        .then((data) => {
            const random_number = data.random_number;
            const binary_representation = data.binary_representation;

            // Update your HTML elements with the retrieved data
            randomNumberElement.textContent = `Random number: ${random_number}`;
            binaryRepresentationElement.textContent = `Binary representation: ${binary_representation}`;
        })
        .catch((error) => console.error("Error fetching data:", error));

        var score = 0
    
        // Store the original innerHTML and styles of each button
        var originalText1 = document.getElementById("b1").innerHTML;
        var originalText2 = document.getElementById("b2").innerHTML;
        var originalText3 = document.getElementById("b3").innerHTML;
        var originalText4 = document.getElementById("b4").innerHTML;
        var originalText5 = document.getElementById("b5").innerHTML;
        var originalText6 = document.getElementById("b6").innerHTML;

        // Define a common function for changing button text and style
        function changeText(buttonId, originalText) {
            var button = document.getElementById(buttonId);

            if (button.innerHTML === originalText) {
                button.innerHTML = "1";
            } else {
                button.innerHTML = originalText;
            }
        }

        // Call the common function for each button click
        function c1() {
            changeText("b1", originalText1);
        }

        function c2() {
            changeText("b2", originalText2);
        }

        function c3() {
            changeText("b3", originalText3);
        }

        function c4() {
            changeText("b4", originalText4);
        }

        function c5() {
            changeText("b5", originalText5);
        }

        function c6() {
            changeText("b6", originalText6);
        }