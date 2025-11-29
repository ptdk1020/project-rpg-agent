from google.adk.tools.tool_context import ToolContext
from typing import Dict, Any

def retrieve_userinfo(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Tool to retrieve user name and preferred setting from session state.
    """
    # Read from session state
    user_name = tool_context.state.get("user:name", "Username not found")
    last_setting_played = tool_context.state.get("user:last_setting_played", "Last setting not found")
    profile_last_updated = tool_context.state.get("user:profile_last_updated", "Last updated not found")

    return {"status": "success", 
            "user_name": user_name, 
            "last_setting_played": last_setting_played,
            "profile_last_updated":profile_last_updated}