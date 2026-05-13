from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("The class was very interesting"))
