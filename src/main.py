from os import environ as env
from sqlite3 import OperationalError
from fastapi import FastAPI
from sqlalchemy import  text

from .utils.helpers import format_size_bytes
from .routers.v1 import ollama_router
from fastapi.middleware.cors import CORSMiddleware
import psutil
from .utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
import time
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

@app.get("/health_status")
def status(db:Session = Depends(get_db)):

    start_time = time.time()

    # Check CPU Usage
    cpu_usage = psutil.cpu_percent(interval=0.1)
    is_busy = cpu_usage > 80  # Adjust threshold as needed

    # Check Database
    db_status = "connected"
    try:
        db.execute(text("SELECT 1"))
    except:
        db_status = "disconnected"

    # Measure API response time
    response_time = time.time() - start_time

    # Determine overall status
    if db_status == "disconnected":
        system_status = "DOWN"
    elif is_busy or response_time > 1.0:
        system_status = "BUSY"
    else:
        system_status = "ALL GOOD"
    disk_usage ={ 
        "useage_percent": f"{psutil.disk_usage('/').percent}%",
        "used": format_size_bytes(psutil.disk_usage("/").used),
        "free": format_size_bytes(psutil.disk_usage("/").free),
    }
    return {
        "status": system_status,
        "cpu_usage": f"{cpu_usage}%",
        "response_time": f"{response_time:.2f}s",
        "database": db_status,
        "disk_usage": disk_usage    
    }
    
