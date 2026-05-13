from gensim.models import Word2Vec

medical_corpus = [
 "patient suffers from diabetes and hypertension",
 "doctor prescribes insulin for diabetes",
 "hypertension increases risk of heart disease",
 "insulin regulates blood sugar levels",
 "patient diagnosed with heart disease"
]
sentences = [s.split() for s in medical_corpus]

model = Word2Vec(
 sentences,
 vector_size=50,
 window=3,
 min_count=1,
 workers=1,
)

print("Similar words to 'diabetes':")
print(model.wv.most_similar("diabetes"))
print("\nSimilar words to 'patient':")
print(model.wv.most_similar("patient"))
