from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool, FunctionTool#, google_search, 

from .config import config
from .agent_tools import (
    world_builder,
    character_creator,
    adventure_planner
)
from .tools import (
    save_userinfo, retrieve_userinfo, db_query, db_insert, update_settings
)

game_master = LlmAgent(
    name="game_master",
    model=config.model,
    instruction="""You are a game master agent, your job is to run player through a 
    choose-your-own adventure role playing game.

    Available tools:
    - `save_userinfo` tool: save user info.
    - `retrieve_userinfo` tool: fetch user info
    - `update_settings` too: update session settings
    - `db_query` tool: fetch information from database
    - `db_insert` tool: insert information into database
    - `world_builder` : world building tool
    - `character_creator`: character creation tool
    - `adventure_planner`: adventure planning tool

    Your exact workflow is as follows:
    1. **World building**: Ask whether player wants to play in an existing world setting
    or a new world. 
        - If existing, use the `db_query` tool to find world setting with appropriate
        theme, if found, update world_setting value with the full document using the `update_settings` tool. 
        - Otherwise, you will generate a world and present it to the player using the `world_builder` tool.
        In this case, DO NOT update settings.
    AFTER confirmed that the user wants to play in the world, use `db_insert` to add this newly 
    created world_setting to the db.
    2. **Character creation**: Use the `character_creator` tool to generate a character
    in the world
    3. Create an adventure using the `adventure_planner` tool.
    4. **Running the game**: Use the created adventure_plan to run the game interactively
    with the player. You have to use the adventure_plan created in step 3.
    At any step, if the player chooses an incorrect choice, it is GAME OVER.
    
    """,
    tools = [AgentTool(agent=world_builder), 
             AgentTool(agent=character_creator),
             AgentTool(agent=adventure_planner),
             FunctionTool(save_userinfo),
             FunctionTool(retrieve_userinfo),
             FunctionTool(db_insert),
             FunctionTool(db_query),
             FunctionTool(update_settings)
             ]
)

root_agent = game_master

async def main():
    from google.adk.runners import InMemoryRunner
    runner = InMemoryRunner(agent=world_builder)
    response = await runner.run_debug(
    "Create a steampunk world"
    )
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
    

