# Flask Application with Prometheus Metrics

This is a simple Flask application that exposes Prometheus metrics and has three routes responding with different HTTP status codes.

## Features

- Exposes `/metrics` for Prometheus.
- Three routes:
  - `/success` (HTTP 200)
  - `/client-error` (HTTP 400)
  - `/server-error` (HTTP 500)

## Requirements

- Python 3.9
- Docker (for containerization)

## Project Structure
my_flask_app/
│
├── app.py
├── Dockerfile
└── requirements.txt

