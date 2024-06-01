from crewai_tools import tool

from tweetcrafter.config import Config


@tool("save_tweet")
def save_tweet(text: str):
    """Save a tweet text to a markdown file."""
    file_path = Config.Path.OUTPUT_DIR / "tweet.md"
    with file_path.open("w") as file:
        file.write(text)
    return file_path


@tool("read_tweets")
def read_tweets() -> str:
    """Read all tweets from a markdown file."""
    with (Config.Path.DATA_DIR / "tweets.md").open("r") as file:
        return file.read()
