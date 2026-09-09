"""
LangGraph Closed-Loop Pipeline Graph Machine
Implements the 6-stage closed loop: Listen -> Extract -> Match -> Act -> Verify -> Confirm.
"""
from app.orchestrator.state import MeetingAgentState, AgentPipelineStage
from app.services.transcription import transcription_service
from app.services.extraction import extraction_service
from app.services.linear_client import linear_client

class ClosedLoopOrchestrator:
    def run_pipeline(self, meeting_id: str, audio_path: str) -> MeetingAgentState:
        state = MeetingAgentState(meeting_id=meeting_id, audio_path=audio_path)

        # Stage 1: LISTEN (Audio Transcribe & Diarize)
        state.current_stage = AgentPipelineStage.LISTEN
        audio_result = transcription_service.process_audio(audio_path)
        state.transcript_segments = audio_result["diarized_segments"]

        # Stage 2: EXTRACT (LLM Task Extraction)
        state.current_stage = AgentPipelineStage.EXTRACT
        state.raw_action_items = extraction_service.extract_action_items(state.transcript_segments)

        # Stage 3: MATCH (Semantic Deduplication)
        state.current_stage = AgentPipelineStage.MATCH
        # Phase 1 simulation: all items are new & non-duplicate
        state.deduped_action_items = state.raw_action_items

        # Stage 4: ACT (Create Linear Tickets)
        state.current_stage = AgentPipelineStage.ACT
        for item in state.deduped_action_items:
            ticket = linear_client.create_ticket(
                title=item["description"],
                description=f"Extracted from Meeting {meeting_id}. Quote: {item.get('source_quote')}",
                assignee=item.get("owner")
            )
            state.created_tickets.append(ticket)

        # Stage 5: VERIFY (Re-fetch & Confirm Ticket State)
        state.current_stage = AgentPipelineStage.VERIFY
        for ticket in state.created_tickets:
            is_valid = linear_client.verify_ticket_state(ticket["ticket_id"], ticket["title"])
            state.verification_results.append({
                "ticket_id": ticket["ticket_id"],
                "status": "confirmed" if is_valid else "mismatch",
                "verified": is_valid
            })

        # Stage 6: CONFIRM (Completed)
        state.current_stage = AgentPipelineStage.CONFIRM
        return state

orchestrator = ClosedLoopOrchestrator()
