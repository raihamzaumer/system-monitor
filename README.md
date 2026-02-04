
#  Flask System Monitor App

A lightweight **system monitoring web application** built with **Flask** that provides real-time insights into server health. This project is designed for **DevOps beginners and backend developers** to demonstrate system observability, containerization, and deployment practices.

##  Features

* CPU usage monitoring
* Memory (RAM) usage tracking
* Disk usage statistics


##  Tech Stack

* **Backend:** Python, Flask
* **System Metrics:** psutil
* **Deployment-ready:** Docker (optional)
* **Cloud-friendly:** AWS EC2 compatible

## 📁 Project Structure

```
system-monitor/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
├── Dockerfile
└── README.md
```

##  Installation & Setup

### 1️ Clone the repository

```bash
git clone https://github.com/your-username/system-monitor.git
cd system-monitor
```

### 2️ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️ Run the application

```bash
python app.py
```

Access the app:

```
http://localhost:5000/api/stats
```

##  API Endpoint

### `GET /api/stats`

Returns real-time system statistics in JSON format.

**Sample Response:**

```json
{
  "cpu_percent": 18.5,
  "memory_percent": 42.1,
  "disk_percent": 63.8,
  
}
```

## Docker Support 

Build image:

```bash
docker build -t flask-system-monitor .
```

Run container:

```bash
docker run -p 5000:5000 flask-system-monitor
```

## Deployment

This application can be deployed on:

* AWS EC2
* Docker containers
* CI/CD pipelines (GitHub Actions)

##  Use Case

* DevOps practice project
* Backend monitoring demo
* Cloud deployment showcase
* Resume & interview portfolio project


##  Contributing

Contributions are welcome. Feel free to fork this repository and submit a pull request.

##  License

This project is licensed under the MIT License.



