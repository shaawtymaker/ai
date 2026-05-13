import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

seed = "technology"
words = [w for w, _ in model.most_similar (seed, topn=5)]

sentence = "Technology is related to " + ", ".join(words) + "."
print(sentence)
print (f"[words[0] is an important part of technology.")
print (f" (words[1]) helps improve our daily life.")
print(f"[words[2]) is widely used in modern systems.")
print (f" (words[3]) plays a key role in innovation.")
print (f" (words (4) makes communication easier.")