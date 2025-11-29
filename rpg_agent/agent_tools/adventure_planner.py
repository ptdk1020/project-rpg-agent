from google.adk.agents import LlmAgent
from ..config import config


adventure_planner = LlmAgent(
    name="adventure_planner",
    model=config.model,
    instruction="""You are a adventure planner agent for a choose-your-own adventure role
    playing game based on the world setting and the player character.

    **World setting:**
    {world_setting}

    **Player Character:**
    {player_character}
    
    Your workflow is as follows:
    1. Come up with an adventure outline of 5 linear events from beginning to adventure end.
    2. For each of the 5 linear events, construct binary choices (1 correct choice and 1 incorrect choice)
    """,
    output_key="adventure_plan"
)