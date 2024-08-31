from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/listings', methods=['GET'])
def get_listings():
    api_key = 'NqsXK0DnQA9zGQu90_vXyVDXnyPJq3qB'  # Ensure this environment variable is set
    url = 'https://csfloat.com/api/v1/listings'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch listings'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Ensure Flask is listening on all network interfaces
