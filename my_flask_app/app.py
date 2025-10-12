from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return "Welcome to the Flask Application!"

@app.route('/success')
def success():
    return jsonify(message="This is a success response."), 200

@app.route('/client-error')
def client_error():
    return jsonify(error="This is a client error."), 400

@app.route('/server-error')
def server_error():
    return jsonify(error="This is a server error."), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)