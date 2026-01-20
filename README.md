Installation
1. Verify Python Installation

Check the installed Python version:

python --version

If Python is not installed, download it from:

https://www.python.org/downloads/

2. Clone or Copy the Project

Copy the project folder to your local machine, for example:

load-tester/

Project structure:

load-tester/
│
├── main.py
├── README.md
└── requirements.txt
3. Install Dependencies

Navigate to the project directory and run:

python -m pip install -r requirements.txt

Contents of requirements.txt:

aiohttp
Running the Server to Be Tested

Before running the load testing application, ensure that the target server is running.

Example: Python Local HTTP Server

Run the following command:

python -m http.server 8000

This will start a local server on port 8000.
The endpoint to be tested will be:

http://localhost:8000

If you are using another framework (Flask, FastAPI, etc.), ensure that:

The server is running properly

The port and endpoint are known

Test Configuration

Open main.py and configure the following parameters:

URL = "http://localhost:8000"
TOTAL_REQUEST = 10000
CONCURRENT = 50
TIMEOUT = 5

Parameter description:

URL: target endpoint to be tested

TOTAL_REQUEST: total number of requests sent

CONCURRENT: number of simultaneous requests

TIMEOUT: response timeout in seconds

Running the Load Test

After the server is running, execute the application:

python main.py
Test Output

Example output:

===== LOAD TEST RESULT =====
Target        : http://localhost:8000
Total Request : 10000
Success       : 9850
Failed        : 150
Duration      : 32.45 seconds
RPS           : 308.14

Output description:

Success: number of requests with HTTP status code 2xx

Failed: requests that failed due to client errors (4xx), server errors (5xx), timeouts, or connection issues

Duration: total execution time of the test

RPS (Requests Per Second): average number of requests processed per second

Testing Objectives

This load testing process is intended to:

Measure server performance under concurrent load

Identify system capacity limits

Observe server stability during high traffic conditions

Security and Ethical Notice

This application must be used only for testing systems owned by the user or systems with explicit authorization.
Using this tool against external systems without permission may violate applicable laws and regulations.