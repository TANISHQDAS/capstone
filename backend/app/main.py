from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from typing import Dict, Any, Optional
from pydantic import BaseModel

from app.config import settings
from app.orchestrator.graph import orchestrator
from app.services.slack_gate import slack_gate

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Backend API for Meeting Intelligence Agent - Closed Loop Automation"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for meetings & action items
meetings_db: Dict[str, Dict[str, Any]] = {}

class ApprovalResponse(BaseModel):
    action: str # 'approve' | 'edit' | 'reject'
    updated_owner: Optional[str] = None
    updated_due_date: Optional[str] = None

@app.get("/")
def read_root():
    return {
        "status": "online",
        "app": settings.APP_NAME,
        "version": settings.VERSION,
        "description": "Closed-loop Meeting Intelligence Agent API"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/meetings")
def list_meetings():
    return {"meetings": list(meetings_db.values())}

@app.get("/meetings/{meeting_id}")
def get_meeting(meeting_id: str):
    if meeting_id not in meetings_db:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meetings_db[meeting_id]

@app.post("/meetings/upload")
async def upload_meeting(file: UploadFile = File(...)):
    meeting_id = str(uuid4())
    filename = file.filename or "uploaded_recording.mp3"
    
    # Run closed-loop agent orchestration pipeline
    result_state = orchestrator.run_pipeline(
        meeting_id=meeting_id,
        audio_path=filename
    )
    
    meeting_record = {
        "id": meeting_id,
        "source": "upload",
        "filename": filename,
        "occurred_at": "2026-09-09T23:13:00Z",
        "participants": ["Alex", "Maya", "Marcus"],
        "pipeline_stage": result_state.current_stage,
        "action_items": result_state.deduped_action_items,
        "tickets": result_state.created_tickets,
        "verifications": result_state.verification_results
    }
    
    meetings_db[meeting_id] = meeting_record
    return {
        "status": "success",
        "meeting": meeting_record
    }

@app.post("/approval/{action_item_id}/respond")
def respond_approval(action_item_id: str, payload: ApprovalResponse):
    result = slack_gate.process_human_response(
        action_item_id=action_item_id,
        action=payload.action,
        updated_owner=payload.updated_owner
    )
    return {
        "status": "success",
        "approval": result
    }
