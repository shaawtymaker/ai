from transformers import pipeline

style_transfer = pipeline(
    "text-generation",
    model="gpt2"
)

sentence = "Hey bro, what's up? Let's catch up later?"

result = style_transfer(
    sentence,
    max_length=50,
    num_return_sequences=3,
    temperature=0.8,
    do_sample=True
)

print("Original sentence:")
print(sentence)

print("\nTransformed Sentence (Formal Style):")
print(result[0]['generated_text'])
