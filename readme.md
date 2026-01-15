# Python Flask API

A simple Flask REST API with math utility endpoints and a complete CI/CD pipeline.

## Features

- Flask REST API with health checks and calculation endpoints
- Comprehensive test suite with pytest
- Automated testing and code quality checks
- Security scanning integration
- Artifact versioning and deployment automation

## Quick Start

### Prerequisites

- Python 3.11 or higher
- pip

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd py-gha

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt
```

### Running the Application

```bash
# Run the Flask app
python app/main.py

# Or using Flask CLI
flask --app app.main run
```

The application will be available at http://localhost:5000

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run with JUnit XML output (for CI)
pytest --junitxml=test-results.xml
```

### Code Quality

```bash
# Format code with Black
black app/ tests/

# Check formatting
black --check app/ tests/

# Run linting
flake8 app/ tests/ --max-line-length=100
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Hello World message |
| `GET /health` | Health check endpoint |
| `GET /api/add/<a>/<b>` | Add two numbers |
| `GET /api/multiply/<a>/<b>` | Multiply two numbers |
| `GET /api/fibonacci/<n>` | Calculate Fibonacci number |

### Example Requests

```bash
# Hello endpoint
curl http://localhost:5000/

# Health check
curl http://localhost:5000/health

# Add numbers
curl http://localhost:5000/api/add/5/3

# Calculate Fibonacci
curl http://localhost:5000/api/fibonacci/10
```

## CI/CD Pipeline

The GitHub Actions workflow provides automated testing, code quality checks, and deployment:

- **Testing**: Automated test execution with coverage reporting
- **Code Quality**: Format checking with Black and linting with Flake8
- **Security**: Black Duck SCA scanning for dependency vulnerabilities
- **Build & Deploy**: Automated versioning, package building, and artifact management

See [.github/workflows/ci.yml](.github/workflows/ci.yml) for the complete pipeline configuration.

## Development

This project uses standard Python development tools:

- **pytest** for testing
- **black** for code formatting
- **flake8** for linting
- **pytest-cov** for coverage reporting

All dependencies are managed via pip and defined in `requirements.txt` and `requirements-dev.txt`.

## License

MIT
