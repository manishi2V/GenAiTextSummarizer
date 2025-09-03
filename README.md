# GenAiTextSummarizer

A simple, ready-to-use text summarization tool using state-of-the-art Large Language Models (LLMs) via Hugging Face Transformers. This project leverages the BART model (`facebook/bart-large-cnn`) to generate concise summaries from long pieces of text. Designed for educational and demonstration purposes, it's ideal for running in Google Colab with GPU support.

## Features

- **Summarization with BART**: Uses the `facebook/bart-large-cnn` model, fine-tuned for summarization tasks.
- **Quick Setup**: Minimal code and dependencies. Works out-of-the-box in Google Colab.
- **Easy to Use**: Single script to summarize any input text.

## Prerequisites

- Python 3.x
- Hugging Face Transformers
- PyTorch

Install dependencies (run in a Colab/Jupyter cell or your terminal):

```bash
pip install transformers torch
```

> **Tip:** For faster inference, enable GPU in Google Colab:  
> Menu > Runtime > Change Runtime Type > Hardware Accelerator > Select `GPU`

## Usage

1. **Clone or open this repository in Google Colab.**
2. **Edit the `text` variable in `main.py` with the content you want to summarize.**
3. **Run the script.**

### Example Code (main.py)

```python
from transformers import pipeline

# Initialize summarization pipeline with BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Input: Long text to summarize
text = """
Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.
Specific applications of AI include expert systems, natural language processing (NLP), speech recognition, and machine vision...
"""

# Generate summary
summary = summarizer(text, max_length=100, min_length=75, do_sample=False)

# Output result
print("Summary:", summary[0]['summary_text'])
```

## Tools and LLMs Used

- **Platform:** Google Colab (recommended for easy GPU access)
- **Model:** [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
- **Library:** [Hugging Face Transformers](https://github.com/huggingface/transformers)
- **Backend:** PyTorch

## Customization

- Change `max_length` and `min_length` in the `summarizer()` call to control the length of your summaries.
- Replace the `text` variable with your own content for summarization.

## License

This project is for educational and demonstration purposes.