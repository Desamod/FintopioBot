from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [3200, 3600]
    START_DELAY: list[int] = [5, 20]
    AUTO_TASK: bool = True
    PLAY_CLICKER: bool = True
    JOIN_TG_CHANNELS: bool = True
    REF_ID: str = 'reflink-reflink_lxr8asPHBD28HyDs-'


settings = Settings()
