from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    AIR_QUALITY_API_KEY: str
    FOURSQUARE_API_KEY: str
    OPENAI_API_KEY: str
    REDIS_URL: str
    REDIS_PORT: int = 6379
    GEOLOCATION_IQ_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    SUPABASE_TABLE: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()