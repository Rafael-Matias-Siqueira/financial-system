from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
async def home():
    return {"status": "ok",
            "application": "Meu Controle Financeiro"}



