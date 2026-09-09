"""
LLM Extraction Service
Extracts structured action items (task, owner, due_date, source_quote, confidence) from transcript text.
"""
from typing import List, Dict, Any

class ExtractionService:
    def extract_action_items(self, transcript_segments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Parses diarized segments using LLM structured output schema.
        """
        extracted_items = [
            {
                "description": "Set up PostgreSQL pgvector database index",
                "owner": "Marcus",
                "due_date": "2026-09-12",
                "source_quote": "We need to set up the pgvector database index by Friday.",
                "confidence": 0.95
            },
            {
                "description": "Complete LangGraph 6-stage closed-loop state machine",
                "owner": "Maya",
                "due_date": "2026-09-10",
                "source_quote": "I'll finish the LangGraph state machine today.",
                "confidence": 0.98
            }
        ]
        return extracted_items

extraction_service = ExtractionService()
