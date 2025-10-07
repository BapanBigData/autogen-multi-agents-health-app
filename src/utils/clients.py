from autogen_ext.models.openai import OpenAIChatCompletionClient
from supabase import create_client, Client
from .config import Config
from .constants import MODEL_OPENAI

model_client = OpenAIChatCompletionClient(
    model=MODEL_OPENAI, temperature=0.0, api_key=Config.OPENAI_API_KEY
)

supabase: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
