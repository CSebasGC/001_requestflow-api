from fastapi import FastAPI

app = FastAPI(
    title="RequestFlow FastAPI",
    description="API backend para la gestión de solicitudes institucionales y empresariales",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return{
        "message":"RequestFlow API is running",
        "project":"Proyecto 001",
        "version":"0.1.0",
        "status":"ok",
    }

@app.get("/health")
def health_check():
    return{
        "status":"healthy",
        "message":"RequestFlow-API",
    }