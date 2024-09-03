from flask import Flask, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

@app.route('/api/listings', methods=['GET'])
def get_listings():
    api_key = 'NqsXK0DnQA9zGQu90_vXyVDXnyPJq3qB'
    all_listings = []

    for i in range(45, 55):
        url = f'https://csfloat.com/api/v1/listings/?page={i}'
        headers = {
            'Authorization': api_key,
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            if isinstance(data, list):
                all_listings.extend(data)
            else:
                return jsonify({'error': 'Unexpected response format'}), 500
            
            # Delay between requests to avoid rate limiting
            time.sleep(2)  # Adjust the sleep time as needed
            
        except requests.RequestException as e:
            return jsonify({'error': f'Failed to fetch listings from page {i}'}), 500

    return jsonify(all_listings)

if __name__ == '__main__':
    app.run()
