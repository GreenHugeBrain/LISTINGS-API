from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/listings', methods=['GET'])
def get_listings():
    api_key = 'NqsXK0DnQA9zGQu90_vXyVDXnyPJq3qB'
    url = 'https://csfloat.com/api/v1/listings'
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch listings'}), response.status_code

if __name__ == '__main__':
    app.run()
