import gensim.downloader as api

model =api.load("glove-wiki-gigaword-50")
seed= "beauty"

words = [w for w,_ in model.most_similar (seed, topn=5)]
story =(
f"In the world of beauty, {words[0]} and {words [1]} come alive, "
f"{words[2]} shines quietly, and {words [3]} and {words [4]} remind us of peace.")

print(story)