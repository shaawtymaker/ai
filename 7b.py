from transformers import pipeline

summarizer = pipeline("summarization")

passage = """ India, country that occupies the greater part of South Asia. It is made up of “28”
states and eight union territories, and its national capital is New Delhi, built in the “20th”
century just south of the historic hub of Old Delhi to serve as India’s administrative center. Its
government is a constitutional republic that represents a highly diverse population consisting
of thousands of ethnic groups and hundreds of languages. India became the world’s most
populous country in “2023”, according to estimates by the United Nations. """

summary = summarizer(passage, max_length=100, min_length=25, do_sample=False)

print(summary[0]['summary_text'])