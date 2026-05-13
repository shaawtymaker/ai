import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

seed = "nature"
words = [w for w,_ in model.most_similar(seed, topn=5)]

sentence = "Nature connects " + ", ".join(words)
print(sentence)