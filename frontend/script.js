// Import library lodash dari CDN
import _ from 'lodash';

document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/api/token_info')  // Sesuaikan port jika diperlukan
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
            <p>Modified with lodash: ${_.capitalize(data.token_name)}</p> <!-- Tambahkan penggunaan lodash di sini -->
            <!-- Tambahkan elemen HTML lain jika diperlukan -->
        `;
    }
});
