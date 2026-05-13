import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")
seed_word = "technology"

similar_words = model.most_similar(seed_word, topn=5)
words = [seed_word] + [w for w, _ in similar_words]

paragraph = f"""
{seed_word.capitalize()} is evolving rapidly. Innovations in {words[1]} and
{words[2]} have transformed modern {words[3]}. The growth of {words[4]} and
{words[5]} continues to shape the future.
"""