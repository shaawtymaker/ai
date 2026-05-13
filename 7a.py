from transformers import pipeline

summarizer = pipeline("summarization")

text = """Artificial intelligence enables machines to think and learn like humans.
It’s trending in the IT sector.
It is also replacing some software jobs.
Its features are interesting and make work simpler, reducing human effort."""

summary = summarizer(text, max_length=20, min_length=10)

print(summary)
