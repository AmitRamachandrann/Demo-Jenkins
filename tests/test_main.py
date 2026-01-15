"""Tests for the Flask application."""

import pytest
from app.main import app, calculate_fibonacci


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    """Test the hello endpoint returns success."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, World!"
    assert data["status"] == "success"


def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["service"] == "py-gha-demo"


def test_add_endpoint(client):
    """Test addition endpoint with various inputs."""
    response = client.get("/api/add/5/3")
    assert response.status_code == 200
    data = response.get_json()
    assert data["operation"] == "add"
    assert data["a"] == 5
    assert data["b"] == 3
    assert data["result"] == 8


def test_add_large_numbers(client):
    """Test addition with large numbers."""
    response = client.get("/api/add/100/250")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 350


def test_multiply_endpoint(client):
    """Test multiplication endpoint."""
    response = client.get("/api/multiply/4/7")
    assert response.status_code == 200
    data = response.get_json()
    assert data["operation"] == "multiply"
    assert data["a"] == 4
    assert data["b"] == 7
    assert data["result"] == 28


def test_multiply_by_zero(client):
    """Test multiplication by zero."""
    response = client.get("/api/multiply/5/0")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 0


def test_fibonacci_endpoint(client):
    """Test Fibonacci calculation endpoint."""
    response = client.get("/api/fibonacci/10")
    assert response.status_code == 200
    data = response.get_json()
    assert data["n"] == 10
    assert data["fibonacci"] == 55


def test_fibonacci_edge_cases(client):
    """Test Fibonacci with edge case values."""
    # Test n=0
    response = client.get("/api/fibonacci/0")
    assert response.status_code == 200
    assert response.get_json()["fibonacci"] == 0

    # Test n=1
    response = client.get("/api/fibonacci/1")
    assert response.status_code == 200
    assert response.get_json()["fibonacci"] == 1


def test_calculate_fibonacci_negative():
    """Test Fibonacci function handles negative numbers."""
    # The function returns 0 for negative values
    assert calculate_fibonacci(-1) == 0
    assert calculate_fibonacci(-5) == 0


def test_fibonacci_too_large_error(client):
    """Test Fibonacci rejects numbers > 50."""
    response = client.get("/api/fibonacci/51")
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_calculate_fibonacci_function():
    """Test the Fibonacci calculation function directly."""
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(2) == 1
    assert calculate_fibonacci(3) == 2
    assert calculate_fibonacci(4) == 3
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(6) == 8
    assert calculate_fibonacci(7) == 13
    assert calculate_fibonacci(10) == 55


def test_calculate_fibonacci_larger_values():
    """Test Fibonacci with larger values."""
    assert calculate_fibonacci(15) == 610
    assert calculate_fibonacci(20) == 6765
