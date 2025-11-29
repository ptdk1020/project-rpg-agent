from google.adk.tools.tool_context import ToolContext
from typing import Dict, Any
from datetime import datetime

def save_userinfo(
    tool_context: ToolContext, user_name: str, last_setting_played: str
) -> Dict[str, Any]:
    """
    Tool to record and save user name and last setting played in session state.

    Args:
        user_name: The username to store in session state
        last_setting_played: the theme of the user's last chosen setting.
    """
    # Write to session state using the 'user:' prefix for user data
    tool_context.state["user:name"] = user_name
    tool_context.state["user:last_setting_played"] = last_setting_played
    tool_context.state["user:profile_last_updated"] = datetime.now()

    return {"status": "success"}