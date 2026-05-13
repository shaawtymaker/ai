from transformers import pipeline

style = pipeline("text-generation", model="gpt2")
result =style ( "I can't attend today",
max_length=50,
num_return_sequences=3
)

for i,r in enumerate(result,1):
    print(f"{i}.{r['generated_text']}")