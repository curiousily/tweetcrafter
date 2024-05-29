from crewai_tools import tool
from langchain_community.tools import DuckDuckGoSearchResults


from tweetcrafter.config import Config

search_tool = DuckDuckGoSearchResults(num_results=10)


@tool("save_tweet")
def save_tweet(text):
    """Save a tweet text to a markdown file."""
    file_path = Config.Path.OUTPUT_DIR / "tweet.md"
    with file_path.open("w") as file:
        file.write(text)
    return file_path


@tool("search tool")
def search(search_query: str) -> str:
    """Search the web for a search query"""
    return search_tool.run(search_query)


@tool("read_tweets")
def read_tweets() -> str:
    """Read saved tweets"""
    with (Config.Path.DATA_DIR / "tweets.md").open("r") as file:
        return file.read()
