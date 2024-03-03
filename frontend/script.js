document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/api/token_info')  // Adjust the port if needed
        .then(response => response.json())
        .then(data => {
            displayTokenInfo(data);
        })
        .catch(error => {
            console.error('Error fetching token info:', error);
        });

    function displayTokenInfo(data) {
        const tokenInfoElement = document.getElementById('tokenInfo');
        tokenInfoElement.innerHTML = `
            <h2>${data.token_name}</h2>
            <p>Balance: ${data.balance}</p>
            <!-- Add other HTML elements as needed -->
        `;
    }
});
