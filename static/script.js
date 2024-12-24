document.getElementById("encrypt-button").addEventListener("click", async function() {
    const text = document.getElementById("text-input").value;
    const shift = parseInt(document.getElementById("shift-input").value);

    if (!text) {
        alert("Please enter text to encrypt.");
        return;
    }

    if (isNaN(shift)) {
        alert("Please enter a valid shift value.");
        return;
    }

    try {
        // Send request to the Python script
        const response = await fetch('/caesar_cipher', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text, shift: shift })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const encryptedText = await response.text();
        document.getElementById("output-text").value = encryptedText;
    } catch (error) {
        console.error('Error:', error);
    }
});
