# CI/CD Demo Project

This repository demonstrates a complete CI/CD flow using Python, Docker, and Jenkins.

## Project Structure

```
cicd-demo/
├── app.py              # Main Python application
├── test_app.py         # Unit tests
├── Dockerfile          # Docker container configuration
├── Jenkinsfile         # Jenkins pipeline definition
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Components

### Python Application (`app.py`)
A simple Python application that demonstrates:
- Greeting functionality
- Basic arithmetic operations
- Clean code structure with functions and docstrings

### Unit Tests (`test_app.py`)
Comprehensive unit tests covering:
- Default and custom parameters
- Edge cases (empty strings, zero values)
- Different data types (integers, floats)
- Positive and negative scenarios

### Dockerfile
Containerizes the application using:
- Python 3.9 slim base image
- Proper dependency management
- Optimized layer caching

### Jenkinsfile
Complete CI/CD pipeline with stages:
1. **Get Code**: Checkout source code from repository
2. **Build Container**: Build Docker image with version tagging
3. **Build Python**: Install Python dependencies
4. **Run Python Program**: Execute the application
5. **Run Unit Tests**: Run all unit tests with verbose output
6. **Archive Artifacts**: Archive project files for deployment

## Running Locally

### Run the Python Application
```bash
python3 app.py
```

### Run Unit Tests
```bash
python3 -m unittest test_app.py -v
```

### Build Docker Container
```bash
docker build -t cicd-demo-app .
```

### Run Docker Container
```bash
docker run cicd-demo-app
```

## Jenkins Setup

1. Create a new Pipeline job in Jenkins
2. Configure the job to use this repository
3. Set the pipeline script from SCM (use Jenkinsfile)
4. Ensure Docker is available on the Jenkins agent
5. Run the pipeline

## Requirements

- Python 3.9+
- Docker (for containerization)
- Jenkins (for CI/CD pipeline)

## Test Results

All 8 unit tests pass successfully:
- ✅ Greeting with default parameter
- ✅ Greeting with custom name
- ✅ Greeting with empty string
- ✅ Addition with positive numbers
- ✅ Addition with negative numbers
- ✅ Addition with mixed values
- ✅ Addition with zero
- ✅ Addition with floating-point numbers
