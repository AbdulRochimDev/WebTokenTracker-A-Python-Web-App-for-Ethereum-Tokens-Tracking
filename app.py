from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

token_data = {
    "token_name": "MyToken",
    "balance": 100,
}

@app.route('/api/token_info')
def get_token_info():
    return jsonify(token_data)

if __name__ == '__main__':
    app.run(debug=True)
