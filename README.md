📋 Project Overview
This project implements a complete CI/CD pipeline for testing a sentiment analysis API. The API uses the Docker image datascientest/fastapi:1.0.0 and analyzes the sentiment of English sentences.

API Endpoints
/status : Checks API status

/permissions : Returns user permissions

/v1/sentiment : Sentiment analysis with an old model

/v2/sentiment : Sentiment analysis with a new model

🏗️ Project Architecture
text
linkedin-docker-project/
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

🚀 Installation and Execution
Prerequisites
Docker

Docker Compose

Git

Installation
Clone the repository:

bash
git clone [REPO_URL]
cd linkedin-docker-project
Give execution permissions to the script:

bash
chmod +x setup.sh
Run the complete pipeline:

bash
./setup.sh
Manual Execution
If you want to execute steps manually:

Download the API image:

bash
docker image pull datascientest/fastapi:1.0.0
Build test images:

bash
docker-compose build
Start containers:

bash
docker-compose up
Clean up the environment:

bash
docker-compose down
📊 Expected Results
After execution, you will get:

api_test.log : Contains detailed logs of all tests

log.txt : Log summary

Console display of test results

🔧 Configuration
Environment Variables
LOG=1 : Enables log writing to api_test.log

API_ADDRESS=fastapi : API service address in Docker network

API_PORT=8000 : API port

Docker Network
The project uses a Docker network named test_network to enable communication between:

The API container

The three test containers

Volumes
A shared volume is used to:

Share logs between test containers

Persist results after execution

🐳 Custom Docker Images
Each test uses a specific Docker image:

test-authentication : Authentication tests

test-authorization : Authorization tests

test-content : Content tests

📝 Technical Notes
Implementation Choices
Language : Python with requests library for simplicity

Test separation : One container per test type for isolation

Centralized logs : Single file for easier analysis

Docker network : Network isolation for security

Error Handling
Code 200 : Success

Code 403 : Authentication failure

Positivity/negativity score validation

🧹 Cleanup
To remove all created containers, images, and volumes:

bash
docker-compose down --rmi all --volumes
📄 License
This project is created as part of a CI/CD module examination.

👥 Authors
Project created for CI/CD module validation using Docker pipelines.
