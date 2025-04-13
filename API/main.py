# app/main.py
from fastapi import FastAPI
from .api import router as audio_router

app = FastAPI(
    title="Behlaf API",
    description="API that accepts an audio file and returns AI response text and processed audio.",
    version="1.0.0"
)
app.include_router(audio_router, prefix="/api")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
