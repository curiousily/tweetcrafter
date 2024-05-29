# TweetCrafter

Write tweets with AI Agents (CrewAI)

## Installation

Clone the repo

```sh
git clone git@github.com:curiousily/tweetcrafter.git
cd tweetcrafter
```

```sh
poetry install
```

## Add API keys

Create a `.env` file in the root of the project and add your Groq and/or OpenAI API keys:

```sh
GROQ_API_KEY=<GROQ_API_KEY>
OPENAI_API_KEY=<OPENAI_API_KEY>
```

## Usage

Go to `app.py` and change the inputs:

```py
inputs = {
    "topic": "Summary of the key new features of Phi-3",
    "urls": [
        "https://huggingface.co/microsoft/Phi-3-vision-128k-instruct",
    ],
    "suggestion": "Focus on the performance and how-to use the model.",
}
```

Run the app:

```sh
poetry run python app.py
```
