from fastapi import FastAPI

app = FastAPI(
    title="Mini Devin API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Mini Devin API is running!"
    }