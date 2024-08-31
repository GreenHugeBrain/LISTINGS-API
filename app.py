from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/listings', methods=['GET'])
def get_listings():
    url = 'https://csfloat.com/api/v1/listings'
    headers = {
        'Authorization': 'Bearer NqsXK0DnQA9zGQu90_vXyVDXnyPJq3qB',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
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
