from google.adk.agents import LlmAgent

from ..config import config


character_creator = LlmAgent(
    name="character_creator",
    model=config.model,
    instruction="""You are a character creator of a choose-your-own adventure
    game. Your job is to help the player with the creation of their character
    that is in accordance with the world setting.
    
    **World setting:** 
    {world_setting}
    
    The final character should have background, motivation, etc. Present the
    character highlights briefly in bullet points.
    """,
    output_key="player_character"
)