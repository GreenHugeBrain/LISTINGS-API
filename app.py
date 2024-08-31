from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/listings', methods=['GET'])
def get_listings():
    url = 'https://csfloat.com/api/v1/listings'
    headers = {
        'Authorization': 'NqsXK0DnQA9zGQu90_vXyVDXnyPJq3qB',
        'Content-Type': 'application/json'
    }
    cookies = {
        'session': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGVhbV9pZCI6Ijc2NTYxMTk5MDk1Mzg0NjI2Iiwibm9uY2UiOjAsImltcGVyc29uYXRlZCI6ZmFsc2UsImlzcyI6ImNzdGVjaCIsImV4cCI6MTcyNTU0Nzk0NX0.1SHRlZKbXXtIaHMz7QK8TNpOu2v8kbaFA9o2UvPhDIw'
    }
    
    response = requests.get(url, headers=headers, cookies=cookies)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch listings', 'details': response.text}), response.status_code

if __name__ == '__main__':
    app.run()
