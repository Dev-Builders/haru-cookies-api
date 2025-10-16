# FastAPI App with PostgreSQL (Docker DB Only)

Este projeto roda a aplicação FastAPI localmente e usa um container Docker para o banco de dados PostgreSQL.

## Instruções

1. Suba o banco de dados:
```bash
docker-compose up -d
```

2. Instale dependências e rode o app:
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

3. Acesse a API:
[http://localhost:8000/docs](http://localhost:8000/docs)