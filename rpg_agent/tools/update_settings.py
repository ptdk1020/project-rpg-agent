from google.adk.tools.tool_context import ToolContext
from typing import Dict, Any
from datetime import datetime

def update_settings(
    tool_context: ToolContext, setting_name: str, new_setting: str
) -> Dict[str, Any]:
    """
    Tool to update session setting.

    Args:
        setting_name: name of session setting to change
        new_setting: value of new setting
    """
    # Write to session state using the 'user:' prefix for user data
    tool_context.state[setting_name] = new_setting

    return {"status": "success"}