import os
from enum import Enum
from pathlib import Path


class Model(Enum):
    GPT_4o = "gpt-4o"
    LLAMA_3 = "Llama3"


class Config:
    class Path:
        APP_HOME = Path(os.getenv("APP_HOME", Path(__file__).parent.parent))
        DATA_DIR = APP_HOME / "data"
        OUTPUT_DIR = APP_HOME / "output"
        LOGS_DIR = APP_HOME / "logs"
        AGENT_LOGS_DIR = LOGS_DIR / "agents"

    MODEL = Model.LLAMA_3
