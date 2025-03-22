from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock', methods=['POST'])
def get_stock():
    symbol = request.form.get('symbol', '').upper()
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({'error': 'API request failed'}), 500
    
    data = response.json()
    if "Time Series (5min)" not in data:
        return jsonify({'error': 'Invalid symbol or API limit reached'}), 400
    
    time_series = data["Time Series (5min)"]
    latest_time = list(time_series.keys())[0]
    latest_data = time_series[latest_time]
    price = latest_data["4. close"]

    return jsonify({
        'symbol': symbol,
        'price': price,
        'time': latest_time
    })

if __name__ == '__main__':
    app.run(debug=True)