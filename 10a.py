from transformers import pipeline

ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
paragraph = "Barack Obama was born in Hawaii and studied at Harvard University in the United States."
entities = ner_pipeline(paragraph)

print("Named Entities:")
for ent in entities:
    print(f"{ent['word']} --> {ent['entity_group']}")
