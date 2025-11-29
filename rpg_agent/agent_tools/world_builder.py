from google.adk.agents import LlmAgent
from google.adk.tools import google_search, FunctionTool

from ..config import config

world_builder = LlmAgent(
    name="world_builder",
    model=config.model,
    instruction="""You are a world builder agent for a choose-your-own adventure role
    playing game. Your ONLY job is to come up with a campaign setting on a given user
    preference.
    
    If the user specified a particular setting, you must use the google_search tool as
    before forming your reply. Otherwise, you need to come up with an original setting.
    
    Present the world overview, species, countries, factions, famous people. You must 
    be concise and your answer must be written in an immersive fashion.
    """,
    output_key="world_setting",
    tools = [google_search]
)