# AI Incident Automation Platform

An AI-powered incident management and automation platform built using FastAPI, OpenAI, and SQLite.

This system analyzes logs, classifies incidents, stores results in a database, and automatically triggers alerts for critical failures.

---

# Features

- AI-powered incident analysis
- Structured JSON responses
- Upload `.txt` and `.log` files
- SQLite database storage
- Incident history retrieval
- Severity-based automation alerts
- REST APIs using FastAPI
- Swagger API documentation
- File validation and error handling

---

# Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn

## AI
- OpenAI API

## Database
- SQLite

## Validation
- Pydantic

---

# Architecture

```text
User Input / Log File
          ↓
FastAPI Backend
          ↓
OpenAI Incident Analysis
          ↓
Severity Classification
          ↓
SQLite Database Storage
          ↓
Critical Alert Automation
```

---

# Project Structure

```text
ai-incident-automation/
│
├── app/
│   ├── main.py
│   ├── ai_service.py
│   ├── database.py
│   ├── alert_service.py
│   └── models.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# API Endpoints

## Analyze Incident

POST `/analyze-incident`

### Request

```json
{
  "log_text": "CRITICAL: Production payment service completely down due to database failure."
}
```

### Response

```json
{
  "input_log": "CRITICAL: Production payment service completely down due to database failure.",
  "analysis": {
    "issue_summary": "Production payment service down due to database failure",
    "root_cause": "Database failure",
    "severity": "Critical",
    "suggested_fix": "Identify and resolve the database failure",
    "next_action": "Engage database administration team"
  }
}
```

---

## Analyze Log File

POST `/analyze-log-file`

Upload `.txt` or `.log` files for AI-powered incident analysis.

### Supported File Types

- `.txt`
- `.log`

---

## Get Incident History

GET `/incidents`

Returns all saved incidents from the SQLite database.

---

# Automation Workflow

```text
Log Input
   ↓
AI Analysis
   ↓
Severity Detection
   ↓
Database Storage
   ↓
Critical Alert Trigger
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/vikhyath2/ai-incident-automation-platform.git
```

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Add Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_api_key
```

## Run Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Learning Outcomes

This project helped build hands-on experience in:

- FastAPI backend development
- REST API architecture
- OpenAI API integration
- AI-powered automation workflows
- File upload handling
- SQLite database operations
- Event-driven alert systems
- Structured JSON API responses
- Git and GitHub workflows
- Backend debugging and validation

---

# Future Improvements

- Slack integration
- Email notifications
- Streamlit dashboard
- Docker support
- Redis + background workers
- Vector database for AI memory
- Kubernetes deployment

---

# Run Locally

```bash
git clone https://github.com/vikhyath2/ai-incident-automation-platform.git

cd ai-incident-automation-platform

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# Author

Vikhyath Vardhan
