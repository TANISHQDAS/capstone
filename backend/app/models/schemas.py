from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# ==========================================
# 5. Data Model (Matching Architecture Plan)
# ==========================================

# --- 5.1 meetings ---
class MeetingBase(BaseModel):
    source: str = Field("upload", description="'zoom' | 'upload'")
    participants: List[str] = Field(default_factory=list, description="Diarized speaker list")

class MeetingCreate(MeetingBase):
    transcript_url: Optional[str] = None

class Meeting(MeetingBase):
    id: UUID = Field(default_factory=uuid4)
    occurred_at: datetime = Field(default_factory=datetime.utcnow)
    transcript_url: Optional[str] = None

    class Config:
        from_attributes = True


# --- 5.2 action_items ---
class ActionItemBase(BaseModel):
    description: str = Field(..., description="Extracted task text")
    owner: Optional[str] = Field(None, description="Best-guess assignee")
    due_date: Optional[str] = Field(None, description="Nullable ISO date string")
    status: str = Field("proposed", description="'proposed' | 'approved' | 'rejected'")

class ActionItemCreate(ActionItemBase):
    meeting_id: UUID

class ActionItem(ActionItemBase):
    id: UUID = Field(default_factory=uuid4)
    meeting_id: UUID
    embedding: Optional[List[float]] = Field(default=None, description="Vector for semantic dedup matching")

    class Config:
        from_attributes = True


# --- 5.3 ticket_links ---
class TicketLinkBase(BaseModel):
    action_item_id: UUID
    external_ticket_id: str = Field(..., description="ID in Linear/Asana/Notion")
    verification_status: str = Field("confirmed", description="'confirmed' | 'mismatch' | 'failed'")

class TicketLinkCreate(TicketLinkBase):
    pass

class TicketLink(TicketLinkBase):
    id: UUID = Field(default_factory=uuid4)
    last_verified_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
