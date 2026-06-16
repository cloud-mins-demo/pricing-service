from flask import Flask
from pricing import calculate_price

app = Flask(__name__)

@app.route("/price")
def price():
    return str(calculate_price())

app.run(port=5000)