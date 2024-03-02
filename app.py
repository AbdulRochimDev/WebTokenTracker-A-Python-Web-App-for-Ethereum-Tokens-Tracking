from flask import Flask, render_template
from TokenTracker import TokenTracker

app = Flask(__name__)
token_tracker = TokenTracker()

@app.route('/')
def index():
    return render_template('index.html', token_holdings=token_tracker.token_holdings)

if __name__ == '__main__':
    app.run(debug=True)
