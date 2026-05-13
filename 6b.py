from transformers import pipeline

sentiment_pipeline=pipeline("sentiment-analysis")

sentences = [
 "I love this product! It's amazing.",
 "This is the worst experience ever.",
 "The weather is okay today.",
 "Fantastic service, highly recommend.",
 "I hate waiting in lines."
]

results = sentiment_pipeline(sentences) 
for sentence, result in zip(sentences, results): 
 print(f"Sentence: '{sentence}'")
 print(f"Sentiment: {result['label']} (confidence: {result['score']:.4f})\n")