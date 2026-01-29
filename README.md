# 📋 Project Overview

This project implements a complete **CI/CD pipeline** for testing a **sentiment analysis API**.  
The API uses the Docker image `datascientest/fastapi:1.0.0` and analyzes the sentiment of English sentences.

---

## 🏗️ Project Structure

```text
├── docker-compose.yml          # Docker Compose configuration
├── setup.sh                    # Installation and launch script
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── api_test.log                # Test logs (generated)
├── log.txt                     # Log results
├── tests/
│   ├── authentication/
│   │   ├── Dockerfile
│   │   └── test_auth.py
│   ├── authorization/
│   │   ├── Dockerfile
│   │   └── test_authz.py
│   └── content/
│       ├── Dockerfile
│       └── test_content.py
└── notes.md                    # Technical choices justifications
🧪 Test Scenarios

1️⃣ Authentication Test
Verifies the authentication logic with three cases:

User alice (password wonderland) → HTTP 200

User bob (password builder) → HTTP 200

User clementine (password mandarine) → HTTP 403

2️⃣ Authorization Test
Verifies access rights to different API versions:

bob → access only to v1

alice → access to v1 and v2

3️⃣ Content Test
Verifies API result accuracy with sample sentences:

"life is beautiful" → positive score

"that sucks" → negative score

🚀 Quick Start
Prerequisites
Docker

Docker Compose

Git

Installation & Execution
bash
Copier le code
# Clone the repository
git clone [REPO_URL]
cd linkedin-docker-project

# Make script executable
chmod +x setup.sh

# Run the complete pipeline
./setup.sh
Manual Execution
bash
Copier le code
# Download API image
docker image pull datascientest/fastapi:1.0.0

# Build and run tests
docker-compose build
docker-compose up
📊 Expected Results
After execution, the following outputs are generated:

api_test.log → detailed logs of all tests

log.txt → summarized test results

Console output displaying test execution status

🔧 Configuration
Environment Variables
Variable	Default	Description
LOG	1	Enables log writing to api_test.log
API_ADDRESS	fastapi	API service address
API_PORT	8000	API port

Docker Network
The project uses a Docker network named test_network to allow communication between containers.

🐳 Docker Images
Image	Purpose
test-authentication	Authentication tests
test-authorization	Authorization tests
test-content	Content validation tests

📝 Code Examples
Sample Test Structure
python
Copier le code
import os
import requests

# API configuration
api_address = os.getenv('API_ADDRESS', 'fastapi')
api_port = os.getenv('API_PORT', 8000)

# Test execution
r = requests.get(
    url=f'http://{api_address}:{api_port}/permissions',
    params={'username': 'alice', 'password': 'wonderland'}
)

# Log results
if os.environ.get('LOG') == '1':
    with open('/logs/api_test.log', 'a') as file:
        file.write(f"Status: {r.status_code}\n")
🧹 Cleanup
bash
Copier le code
# Remove all containers, images, and volumes
docker-compose down --rmi all --volumes
📄 License
This project was created as part of a CI/CD module examination.
