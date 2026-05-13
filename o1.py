import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
word = "computer"
similar_words = model.most_similar(word, topn=5)
print("Similar words to:", word)
for w, score in similar_words:
 print(w, ":", score)