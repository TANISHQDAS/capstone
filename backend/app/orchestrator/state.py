"""
LangGraph Closed-Loop Pipeline State Definition
"""
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class AgentPipelineStage:
    LISTEN = "LISTEN"
    EXTRACT = "EXTRACT"
    MATCH = "MATCH"
    APPROVAL = "APPROVAL"
    ACT = "ACT"
    VERIFY = "VERIFY"
    CONFIRM = "CONFIRM"

class MeetingAgentState(BaseModel):
    meeting_id: str
    audio_path: Optional[str] = None
    transcript_segments: List[Dict[str, Any]] = Field(default_factory=list)
    raw_action_items: List[Dict[str, Any]] = Field(default_factory=list)
    deduped_action_items: List[Dict[str, Any]] = Field(default_factory=list)
    approved_items: List[Dict[str, Any]] = Field(default_factory=list)
    created_tickets: List[Dict[str, Any]] = Field(default_factory=list)
    verification_results: List[Dict[str, Any]] = Field(default_factory=list)
    current_stage: str = AgentPipelineStage.LISTEN
    retry_count: int = 0
    error_message: Optional[str] = None
