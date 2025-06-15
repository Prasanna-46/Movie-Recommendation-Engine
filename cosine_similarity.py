from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["London Paris London", "Paris Paris London"]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(text)
print(count_matrix.toarray())

cosine_sim = cosine_similarity(count_matrix)

print("Cosine Similarity Matrix: \n", cosine_sim)