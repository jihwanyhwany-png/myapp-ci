from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "message": "hello from CI/CD"}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}


# Github Access Key 및 Secret 제거 후 동작 체크