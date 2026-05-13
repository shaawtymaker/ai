from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
sentences = [
 "I love this course",
 "This subject is difficult",
 "The exam is tomorrow"
]
for sent in sentences:
 result = sentiment_pipeline(sent)
 print(f"Sentence: {sent}")
 print(f"Sentiment: {result[0]['label']} | Score: {result[0]['score']:.2f}\n")
