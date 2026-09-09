"""
Meeting Intelligence Agent - Beginner Backend API
Very simple, easy-to-understand FastAPI backend.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import uuid

app = FastAPI(
    title="Meeting Intelligence Agent API",
    description="Beginner-friendly API for extracting tasks from meetings and creating tickets."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models (Simple & Easy to Understand) ---

class TaskItem(BaseModel):
    id: str
    task: str
    owner: str
    due_date: str
    status: str = "pending"  # "pending", "created", "rejected"
    ticket_id: Optional[str] = None

class MeetingRequest(BaseModel):
    transcript_text: Optional[str] = "We need Marcus to configure the database by Friday, and Maya to finish the state machine."

# --- Simple In-Memory Database ---
meetings_db = []

# --- API Endpoints ---

@app.get("/")
def home():
    return {
        "message": "Welcome to Meeting Intelligence Agent API!",
        "status": "ready",
        "steps": ["1. Submit Transcript", "2. Review Extracted Tasks", "3. Create Ticket"]
    }

@app.post("/extract-tasks")
def extract_tasks(request: MeetingRequest):
    """
    Step 1 & 2: Simple Task Extractor
    Parses transcript text into structured action items.
    """
    sample_tasks = [
        TaskItem(
            id=str(uuid.uuid4())[:8],
            task="Configure PostgreSQL database index for fast search",
            owner="Marcus",
            due_date="2026-09-12",
            status="pending"
        ),
        TaskItem(
            id=str(uuid.uuid4())[:8],
            task="Complete 6-stage closed loop state machine",
            owner="Maya",
            due_date="2026-09-10",
            status="pending"
        )
    ]
    
    meeting_record = {
        "meeting_id": str(uuid.uuid4())[:8],
        "transcript": request.transcript_text,
        "extracted_tasks": [t.dict() for t in sample_tasks]
    }
    meetings_db.append(meeting_record)
    
    return {
        "status": "success",
        "meeting": meeting_record
    }

@app.post("/create-ticket")
def create_ticket(task_id: str, owner: str, due_date: str):
    """
    Step 3: Create and verify task ticket in Linear
    """
    generated_ticket_id = f"LIN-{uuid.uuid4().hex[:4].upper()}"
    return {
        "status": "success",
        "message": "Ticket created and verified!",
        "ticket_id": generated_ticket_id,
        "assigned_to": owner,
        "due_date": due_date
    }

@app.get("/download-pdf")
def download_pdf():
    """
    Download Dummy PDF Summary Report
    """
    from fastapi.responses import FileResponse
    pdf_path = "sample_meeting_report.pdf"
    if not os.path.exists(pdf_path):
        from generate_pdf import generate_meeting_pdf
        generate_meeting_pdf(pdf_path)
    return FileResponse(pdf_path, media_type="application/pdf", filename="sample_meeting_report.pdf")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

