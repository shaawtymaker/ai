from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "valhalla/t5-base-qg-hl"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

input_text = "Albert Einstein was born in <hl> Germany <hl>."

inputs = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(inputs["input_ids"], max_length=64, num_beams=4, early_stopping=True)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Generated Text:")
print(generated_text)