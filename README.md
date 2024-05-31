# TweetCrafter

Write tweets with AI Agents (CrewAI)

<a href="https://www.mlexpert.io/bootcamp" target="_blank">
  <img src="https://raw.githubusercontent.com/curiousily/tweetcrafter/master/.github/tweetcrafter.png">
</a>

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

Add tweets to analyze their writing style in `data/tweets.md`:

```md
# Tweet

Ever wondered how to reproduce GPT-2 (124M) efficiently?
@karpathy with llm.c has the answer!

- 90 mins, $20 on 8X A100 80GB SXM
- FineWeb dataset: 10B tokens
- MFU: 49-60%, 178K tokens/sec

https://github.com/karpathy/llm.c/discussions/481
```

Run the app:

```sh
poetry run python app.py
```

```py
{
  'total_tokens': 14322,
  'prompt_tokens': 11767,
  'completion_tokens': 2555,
  'successful_requests': 10
}
```

## Result

The tweets I got from the crew (saved to `output/tweet.md`):

```md
Original Tweet:
"Meet Phi-3, the cutting-edge language model! 🤖💻 With its conversational format, Phi-3 enables human-like text generation, summarization, and more. Scalable, open-source, and responsible AI-driven. 🚀💡 #Phi3 #LanguageModel #AI #NLP"

Version 1:
"Unlock the power of Phi-3! 🚀💻 This cutting-edge language model enables human-like text generation, summarization, and more. Learn how to integrate it into your applications today! 💡 #Phi3 #LanguageModel #AI #NLP"

Version 2:
"Take your applications to the next level with Phi-3! 🚀💻 This scalable, open-source language model enables conversational AI, text generation, and more. Get started with our sample inference code! 💡 #Phi3 #LanguageModel #AI #NLP"

Version 3:
"Discover the possibilities of Phi-3! 🤖💻 This responsible AI-driven language model enables human-like text generation, summarization, and more. Learn how to use it for your next project! 💡 #Phi3 #LanguageModel #AI #NLP"
```

## Observability

_TweetCrafter_ stores logs of prompts and individual agent logs in the `logs` directory.
