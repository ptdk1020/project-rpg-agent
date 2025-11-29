from dataclasses import dataclass, field
from dotenv import load_dotenv
from google.genai import types
from google.adk.models.google_llm import Gemini

load_dotenv()

def _retry_config(): 
    return types.HttpRetryOptions(
        attempts=5,
        exp_base=7,
        initial_delay=1,
        http_status_codes=[429, 500, 503, 504]
        )   

def _model():
    return Gemini(
        model="gemini-2.5-flash",
        retry_options= _retry_config()
        )

@dataclass
class Config:
    retry_config : types.HttpRetryOptions = field(
        default_factory= _retry_config
        )
    model : Gemini = field(
        default_factory= _model
        )

config = Config()