from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from tweetcrafter.callbacks import LLMCallbackHandler
from tweetcrafter.config import Config, Model


def create_model(model: Model):
    callback = LLMCallbackHandler(Config.Path.LOGS_DIR / "prompts.jsonl")
    if model == Model.LLAMA_3:
        return ChatGroq(
            temperature=0,
            model_name="llama3-70b-8192",
            callbacks=[callback],
        )
    elif model == Model.GPT_4o:
        return ChatOpenAI(
            temperature=0,
            model="gpt-4o",
            callbacks=[callback],
        )
