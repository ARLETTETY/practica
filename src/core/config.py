from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = 'practica'
    PROJECT_VERSION: str = '0.0.1'
    DATABASE_URL: str
    
    model_config = {
        "env_file": ".env",
            }

settings = Settings()