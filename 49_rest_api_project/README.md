# 49_rest_api_project

A minimal FastAPI app that runs a small notes API.

How to run:
- pip install -r requirements.txt
- uvicorn main:app --reload --port 8000

Endpoints:
- POST /notes
- GET /notes
- GET /notes/{id}

Improvement suggestion:
- Add persistent storage (SQLite) and authentication.
