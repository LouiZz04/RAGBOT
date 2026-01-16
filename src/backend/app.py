from fastapi import FastAPI, UploadFile, File
from main import get_response, implement_RAG
import shutil
import os

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):

    # on startup

    yield # Running application

    # on shutdown
    for path in (UPLOAD_DIR, "data"):
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"Deleted {path}")


app = FastAPI(lifespan=lifespan)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    paths = []

    for file in files:
        path = os.path.join(UPLOAD_DIR, file.filename)
        with open(path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        paths.append(path)

    # run embeddings
    for path in paths:
        implement_RAG(path)

    return {"status": "indexed", "files": paths}



@app.post("/ask")
def ask(question: str):
    answer = get_response(question)
    return {"answer": answer}

