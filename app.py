from flask import Flask, jsonify
import requests

app = Flask(__name__)

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
        
        response = requests.get(url, headers=headers)
    
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                all_listings.extend(data)
            else:
                return jsonify({'error': 'Unexpected response format'}), 500
        else:
            return jsonify({'error': f'Failed to fetch listings from page {i}'}), response.status_code

    return jsonify(all_listings)

if __name__ == '__main__':
    app.run()
