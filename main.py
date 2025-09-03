# import library
from transformers import pipeline

# Initialize model pipeline. Bart is specifically designed for summarization tasks.
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Decalare the text you wish to summarize. This should be a lengthy and informative piece to test the capability of the model.
text = """
Artifical Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. Specific applications of AI include expert systems, natural language processing, speech recognition and machine vision. AI is part of the broader field of computer science. Artificial intelligence (AI) is a transformative field of computer science focused on creating intelligent machines capable of performing tasks that typically require human intelligence, such as learning, problem-solving, perception, and decision-making, leveraging advanced algorithms and vast datasets to enable applications ranging from natural language processing and computer vision to robotics and autonomous systems, with the potential to revolutionize industries, enhance human capabilities, and address complex global challenges while also raising important ethical considerations regarding bias, privacy, and the future of work, driving continuous research and development to unlock its full potential and ensure its responsible deployment for the benefit of humanity.
"""
# Declare summarizer pipeline
summary = summarizer(text, max_length=100, min_length=75, do_sample=False)

# Print the summary
print("Summary:", summary[0]['summary_text'])
