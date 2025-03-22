document.getElementById('stockForm').addEventListener('submit', function(event) {
  event.preventDefault();
  
  const symbol = document.getElementById('symbol').value;
  const resultDiv = document.getElementById('result');
  
  const formData = new FormData();
  formData.append('symbol', symbol);
  
  fetch('/get_stock', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      if (data.error) {
          resultDiv.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
      } else {
          resultDiv.innerHTML = `
              <p>Stock: ${data.symbol}</p>
              <p>Price: $${data.price}</p>
              <p>Time: ${data.time}</p>
          `;
      }
  })
  .catch(error => {
      resultDiv.innerHTML = `<p style="color: red;">Error: Failed to fetch data</p>`;
      console.error('Error:', error);
  });
});