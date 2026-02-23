from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "message": "hello from CI/CD"}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}