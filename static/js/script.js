async function generateQuote() {
    const category = document.getElementById('category').value;
    const response = await fetch('/quote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ category })
    });
    const data = await response.json();
    document.getElementById('quoteBox').innerText = data.quote;
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}