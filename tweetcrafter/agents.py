from textwrap import dedent

from crewai import Agent
from crewai_tools import ScrapeWebsiteTool

from tweetcrafter.callbacks import step_callback
from tweetcrafter.config import Config
from tweetcrafter.tools import read_tweets, save_tweet

scrape_tool = ScrapeWebsiteTool()


def scraper_agent(llm) -> Agent:
    return Agent(
        role="Senior Website Scraper",
        goal="Scrape the content from the provided URLs and return the text data",
        backstory=dedent("""
            You are an experienced software engineer who is master at scraping various web data (sites, images, videos).
            Your role is to read the content from provided URLs using `scrape_tool` and extract the text.
        """),
        llm=llm,
        tools=[scrape_tool],
        allow_delegation=False,
        step_callback=lambda response: step_callback(
            response, "scrape_agent", Config.Path.AGENT_LOGS_DIR / "scraper.jsonl"
        ),
    )


def researcher_agent(llm) -> Agent:
    return Agent(
        role="Senior Technical Researcher",
        goal="Extract the key insights and information from the internet on the given topic and provided URLs",
        backstory=dedent("""
            You are a technical researcher with expertise in technologies like
            Artificial Intelligence, Machine Learning, Large Language Models etc.
            Your role is to summarize the key insights from the provided texts that are related to the given topic.
        """),
        llm=llm,
        allow_delegation=False,
        step_callback=lambda response: step_callback(
            response,
            "researcher_agent",
            Config.Path.AGENT_LOGS_DIR / "researcher.jsonl",
        ),
    )


def writer_agent(llm) -> Agent:
    return Agent(
        role="Senior Social Media Writer",
        goal=dedent("""
            Write a tweet post based on the research content provided by the Researcher.
            Use the `read_tweets` tool to read all tweets - the tool doesn't have arguments. Emulate the
            writing style of the tweets in your own writing - word choice, formatting, use of emojis, hashtags, etc.
            """),
        backstory=dedent("""
            You have extensive experience in writing engaging content for social media platforms like Twitter, Facebook, Instagram, etc.
            Your main focus is technology - Artificial Intelligence, Machine Learning, Large Language Models etc.
            Your have a track record of writing tweets that engage the audience and drive traffic.
            """),
        llm=llm,
        allow_delegation=False,
        tools=[read_tweets],
        step_callback=lambda response: step_callback(
            response, "writer_agent", Config.Path.AGENT_LOGS_DIR / "writer.jsonl"
        ),
    )


def editor_agent(llm) -> Agent:
    return Agent(
        role="Senior Tweet Editor",
        goal=dedent("""
                Write 3 different versions of the tweet based on the the original research report.
                Keep the format and style of the original tweet.
                Create a single text that contains all variants (original and different versions) of the tweet.
                Use the `save_tweet` and use the `text` parameter to save the text.
            """),
        backstory=dedent("""
            You have experience with social media and understand the importance of engaging content.
            You always write tweets that get a lot of engagement and you are known for your creative writing style.
            """),
        llm=llm,
        allow_delegation=False,
        tools=[save_tweet],
        step_callback=lambda response: step_callback(
            response, "writer_agent", Config.Path.AGENT_LOGS_DIR / "editor.jsonl"
        ),
    )
