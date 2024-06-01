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

Install iPython kernel:

```sh
poetry run python -m ipykernel install --user --name tweetcrafter --display-name "Python (tweetcrafter)"
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
   "total_tokens":12334,
   "prompt_tokens":10260,
   "completion_tokens":2074,
   "successful_requests":8
}
```

## Result

The tweets I got from the crew (saved to `output/tweet.md`):

```md
Original Tweet:
"Meet Phi-3, the cutting-edge AI model revolutionizing NLP! 🚀💻
• Processes human language efficiently and accurately
• Ideal for NLP, text gen, conversational AI, sentiment analysis, and language translation
• Transparent, accountable, and fair decision-making
• Trained on diverse datasets and compatible with TensorFlow and PyTorch
#Phi3 #AI #NLP #LanguageModel #ResponsibleAI

Version 1:
"Unlock the power of Phi-3, the AI model that's changing the NLP game! 🚀💻
• Efficient and accurate language processing
• Perfect for text gen, conversational AI, sentiment analysis, and language translation
• Transparency, accountability, and fairness in decision-making
• Compatible with TensorFlow and PyTorch
#Phi3 #AI #NLP #LanguageModel #ResponsibleAI

Version 2:
"Take your NLP projects to the next level with Phi-3! 🚀💻
• Fast and accurate language processing
• Ideal for conversational AI, sentiment analysis, and language translation
• Built with transparency, accountability, and fairness in mind
• Compatible with TensorFlow and PyTorch
#Phi3 #AI #NLP #LanguageModel #ResponsibleAI

Version 3:
"Discover the future of NLP with Phi-3! 🚀💻
• Efficient language processing for text gen, conversational AI, and more
• Transparent, accountable, and fair decision-making
• Trained on diverse datasets and compatible with TensorFlow and PyTorch
• Revolutionize your NLP projects with Phi-3
#Phi3 #AI #NLP #LanguageModel #ResponsibleAI
```

## Observability

_TweetCrafter_ stores logs of prompts and individual agent logs in the `logs` directory.

Have a look at the `notebooks/explore-logs.ipynb` notebook to explore the logs.
