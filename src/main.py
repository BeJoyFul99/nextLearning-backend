from os import environ as env
from fastapi import FastAPI
from .routers.v1 import ollama_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

# routes
app.include_router(ollama_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"hihi": f"World"}

