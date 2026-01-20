# 🚀 Python Async Load Tester

A lightweight **asynchronous load testing tool** built with Python and `aiohttp`.
This project helps you measure how well a server performs under concurrent traffic by sending thousands of requests efficiently and reporting clear performance metrics.

---

## 📌 Features

* ⚡ Asynchronous HTTP requests using `aiohttp`
* 📊 Clear test summary with success, failure, duration, and RPS
* 🔧 Simple configuration directly in `main.py`
* 🧪 Ideal for local development and performance testing
* 🐍 Minimal dependencies

---

## 🛠️ Installation

### 1. Verify Python Installation

Check your Python version:

```bash
python --version
```

If Python is not installed, download it from:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### 2. Clone or Copy the Project

Copy the project folder to your local machine, for example:

```bash
load-tester/
```

**Project structure:**

```
load-tester/
│
├── main.py
├── README.md
└── requirements.txt
```

---

### 3. Install Dependencies

Navigate to the project directory and install the required packages:

```bash
python -m pip install -r requirements.txt
```

**Contents of `requirements.txt`:**

```
aiohttp
```

---

## 🖥️ Running the Server to Be Tested

Before running the load tester, make sure the target server is running.

### Example: Python Local HTTP Server

You can quickly start a local test server with:

```bash
python -m http.server 8000
```

This will start a server on port **8000**.

**Target endpoint:**

```
http://localhost:8000
```

If you are using another framework (Flask, FastAPI, etc.), ensure that:

* ✅ The server is running properly
* ✅ The port and endpoint are known

---

## ⚙️ Test Configuration

Open `main.py` and configure the following parameters:

```python
URL = "http://localhost:8000"
TOTAL_REQUEST = 10000
CONCURRENT = 50
TIMEOUT = 5
```

### Parameter Description

* **URL**: Target endpoint to be tested
* **TOTAL_REQUEST**: Total number of requests to send
* **CONCURRENT**: Number of simultaneous requests
* **TIMEOUT**: Response timeout in seconds

---

## ▶️ Running the Load Test

Once the server is running, execute:

```bash
python main.py
```

---

## 📈 Test Output

### Example Output

```
===== LOAD TEST RESULT =====
Target        : http://localhost:8000
Total Request : 10000
Success       : 9850
Failed        : 150
Duration      : 32.45 seconds
RPS           : 308.14
```

### Output Description

* **Success**: Number of requests with HTTP status code `2xx`
* **Failed**: Requests that failed due to:

  * Client errors (`4xx`)
  * Server errors (`5xx`)
  * Timeouts or connection issues
* **Duration**: Total execution time of the test
* **RPS (Requests Per Second)**: Average number of requests processed per second

---

## 🎯 Testing Objectives

This load testing tool is designed to:

* Measure server performance under concurrent load
* Identify system capacity and bottlenecks
* Observe server stability during high traffic conditions

---

## 🔐 Security & Ethical Notice

⚠️ **Important**

This application must be used **only** for testing:

* Systems you own, **or**
* Systems for which you have **explicit authorization**

Using this tool against external systems without permission may violate applicable laws and regulations.

---

## 📄 License

This project is provided for educational and testing purposes.
Feel free to modify and extend it to suit your needs.

Happy testing! 🚀
