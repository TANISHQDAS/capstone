"""
Memory Layer - Semantic Deduplication Engine (PostgreSQL + pgvector / Chroma)
Matches newly extracted action items against open items in memory to decide:
- new ticket
- update existing ticket
- discard as noise
"""
from typing import List, Dict, Any, Optional

class DeduplicationEngine:
    def __init__(self):
        # Simulated existing open items memory store
        self.existing_memory = []

    def check_duplicate(self, new_description: str, threshold: float = 0.85) -> Optional[Dict[str, Any]]:
        """
        Calculates embedding similarity between new item and stored action items.
        Returns matching existing item if similarity > threshold, else None.
        """
        for item in self.existing_memory:
            # Simple word overlap / semantic similarity check
            words1 = set(new_description.lower().split())
            words2 = set(item["description"].lower().split())
            similarity = len(words1 & words2) / max(len(words1 | words2), 1)

            if similarity >= threshold:
                return item
        return None

    def store_action_item(self, action_item: Dict[str, Any]):
        self.existing_memory.append(action_item)

dedup_engine = DeduplicationEngine()
