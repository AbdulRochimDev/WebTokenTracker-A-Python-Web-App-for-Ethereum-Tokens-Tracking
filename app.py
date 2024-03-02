from flask import Flask, render_template, jsonify
from token_tracker import TokenTracker  # Ganti dengan nama file sebenarnya

app = Flask(__name__)
token_tracker = TokenTracker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/token_info')
def get_token_info():
    # Ambil informasi token dari token_tracker
    token_info = token_tracker.token_holdings
    return jsonify(token_info)

if __name__ == '__main__':
    app.run(debug=True)
