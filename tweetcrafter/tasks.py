from textwrap import dedent
from typing import List

from crewai import Agent, Task


def scrape_content_task(agent: Agent) -> Task:
    return Task(
        description=("Scrape the text from the provided urls {urls}."),
        expected_output="List of the scraped text from the urls.",
        agent=agent,
    )


def research_content_task(agent: Agent) -> Task:
    return Task(
        description=(
            dedent("""
            Use the scraped content to write a research report on the topic {topic}.
            """)
        ),
        expected_output="Report with well-structured and accurate content on the topic.",
        agent=agent,
    )


def write_tweet_task(agent: Agent, context: List[Task] = []) -> Task:
    return Task(
        description=dedent("""
            Write the tweet based on the research report and writing style based of the tweets.
            Highlight the main technical details in a bullet list that is engaging and easy to understand.
            Use upto 240 characters. Include relevant hashtags and emojis.
        """),
        expected_output="Text of the tweet.",
        agent=agent,
        context=context,
    )


def edit_task(agent: Agent, context: List[Task] = []) -> Task:
    return Task(
        description=dedent("""
            Create 3 different versions of the tweet based on your critique, the original research report,
            and the suggestion {suggestion}. Save the original tweet and 3 versions of the tweet.
        """),
        expected_output="Saved original tweet and 3 versions of the tweet into a text file.",
        agent=agent,
        context=context,
    )
