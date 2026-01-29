📋 Project Overview
This project implements a complete CI/CD pipeline for testing a sentiment analysis API. The API uses the Docker image datascientest/fastapi:1.0.0 and analyzes the sentiment of English sentences.

🏗️ Project Structure
text
├── docker-compose.yml          # Docker Compose configuration
├── setup.sh                    # Installation and launch script
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── api_test.log               # Test logs (generated)
├── log.txt                    # Log results
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
└── notes.md                   # Technical choices justifications
🧪 Test Scenarios
1. Authentication Test
Verifies the authentication logic with three cases:

User alice (password wonderland) → code 200

User bob (password builder) → code 200

User clementine (password mandarine) → code 403

2. Authorization Test
Verifies access rights to different API versions:

bob → access only to v1

alice → access to both versions (v1 and v2)

3. Content Test
Verifies API result accuracy with sentences:

"life is beautiful" → positive score

"that sucks" → negative score

🚀 Quick Start
Prerequisites
Docker

Docker Compose

Git

Installation & Execution
bash
# Clone the repository
git clone [REPO_URL]
cd linkedin-docker-project

# Make script executable
chmod +x setup.sh

# Run the complete pipeline
./setup.sh
Manual Execution
bash
# Download API image
docker image pull datascientest/fastapi:1.0.0

# Build and run tests
docker-compose build
docker-compose up
📊 Expected Results
After execution, you will get:

api_test.log → Contains detailed logs of all tests

log.txt → Log summary

Console display of test results

🔧 Configuration
Environment Variables
Variable	Default	Description
LOG	1	Enables log writing to api_test.log
API_ADDRESS	fastapi	API service address
API_PORT	8000	API port
Docker Network
The project uses a Docker network named test_network to enable communication between containers.

🐳 Docker Images
Image	Purpose
test-authentication	Authentication tests
test-authorization	Authorization tests
test-content	Content validation tests
📝 Code Examples
Sample Test Structure
python
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
# Remove all containers, images, and volumes
docker-compose down --rmi all --volumes
📄 License
This project is created as part of a CI/CD module examination.
