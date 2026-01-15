"""Simple Flask application for CloudBees Unify demo."""

from flask import Flask, jsonify
from typing import Dict, Any


app = Flask(__name__)


@app.route("/")
def hello() -> Dict[str, str]:
    """Return a simple hello message."""
    return jsonify({"message": "Hello, World!", "status": "success"})


@app.route("/health")
def health() -> Dict[str, str]:
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "py-gha-demo"})


@app.route("/api/add/<int:a>/<int:b>")
def add(a: int, b: int) -> Dict[str, Any]:
    """Add two numbers together."""
    result = a + b
    return jsonify({"operation": "add", "a": a, "b": b, "result": result})


@app.route("/api/multiply/<int:a>/<int:b>")
def multiply(a: int, b: int) -> Dict[str, Any]:
    """Multiply two numbers together."""
    result = a * b
    return jsonify({"operation": "multiply", "a": a, "b": b, "result": result})


def calculate_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


@app.route("/api/fibonacci/<int:n>")
def fibonacci(n: int) -> Dict[str, Any]:
    """Calculate Fibonacci number at position n."""
    if n < 0:
        return jsonify({"error": "n must be non-negative"}), 400
    if n > 50:
        return jsonify({"error": "n must be <= 50"}), 400

    result = calculate_fibonacci(n)
    return jsonify({"n": n, "fibonacci": result})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
