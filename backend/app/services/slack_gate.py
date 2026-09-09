"""
Human Approval Gate (Slack Bolt SDK)
Generates Slack Block Kit approval messages before any ticket is created or modified.
Buttons: Approve, Edit, Reject.
"""
from typing import Dict, Any, Optional

class SlackApprovalGate:
    def create_approval_payload(self, action_item: Dict[str, Any]) -> Dict[str, Any]:
        """
        Formats Slack message payload with Approve, Edit, and Reject interactive buttons.
        """
        return {
            "channel": "#meeting-approvals",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "⚡ Meeting Intelligence Agent: Action Item Proposed"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {"type": "mrkdwn", "text": f"*Task:* {action_item['description']}"},
                        {"type": "mrkdwn", "text": f"*Assignee:* {action_item.get('owner', 'Unassigned')}"},
                        {"type": "mrkdwn", "text": f"*Due Date:* {action_item.get('due_date', 'None')}"},
                        {"type": "mrkdwn", "text": f"*Status:* {action_item.get('status', 'proposed')}"}
                    ]
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "✅ Approve"},
                            "style": "primary",
                            "value": f"approve_{action_item.get('id', 'temp')}"
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "✏️ Edit"},
                            "value": f"edit_{action_item.get('id', 'temp')}"
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "❌ Reject"},
                            "style": "danger",
                            "value": f"reject_{action_item.get('id', 'temp')}"
                        }
                    ]
                }
            ]
        }

    def process_human_response(self, action_item_id: str, action: str, updated_owner: Optional[str] = None) -> Dict[str, Any]:
        """
        Handles approval checkpoint decision (approve, edit, or reject).
        """
        return {
            "action_item_id": action_item_id,
            "action": action, # 'approve' | 'edit' | 'reject'
            "updated_owner": updated_owner,
            "status": "approved" if action in ["approve", "edit"] else "rejected"
        }

slack_gate = SlackApprovalGate()
