from fastapi import FastAPI
from app.routers import detect, queue, process
from app.routers import handwriting

app = FastAPI(
    title="Dyslexia Detection API",
    description="API for detecting dyslexia using video, audio, and questionnaires.",
    version="1.0.0"
)
from app.routers import handwriting
from app.routers import dictation



# Include routers
app.include_router(detect.router)
app.include_router(queue.router)
app.include_router(process.router)
app.include_router(handwriting.router)
app.include_router(dictation.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Dyslexia Detection API!"}
