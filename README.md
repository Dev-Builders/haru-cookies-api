This project runs the FastAPI application locally and uses a Docker container for the PostgreSQL database.

## Instructions

1. Start the database:

```bash
docker-compose up -d
```

2. Install dependencies and run the app:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

3. Access the API:
   [http://localhost:8000/docs](http://localhost:8000/docs)
