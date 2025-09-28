from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
movies = {
    "Inception": "sci-fi thriller dream mind heist",
    "Interstellar": "space sci-fi time black hole",
    "The Dark Knight": "action crime superhero batman",
    "Tenet": "time inversion sci-fi action",
    "The Prestige": "magic illusion rivalry drama",
    "Gravity": "space survival astronaut thriller"
}

# Convert movie descriptions to a list
movie_titles = list(movies.keys())
movie_descriptions = list(movies.values())

# Vectorize the descriptions
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movie_descriptions)

# Compute similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix)

def recommend(movie_name, top_n=3):
    # Normalize input
    movie_name = movie_name.strip().lower()

    # Create a lookup dictionary with lowercase keys
    title_lookup = {title.lower(): title for title in movie_titles}

    if movie_name not in title_lookup:
        return "Movie not found in database."

    actual_title = title_lookup[movie_name]
    idx = movie_titles.index(actual_title)
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i, score in similarity_scores[1:top_n+1]:
        recommendations.append(movie_titles[i])

    return recommendations

# Example usage
if __name__ == "__main__":
    print("🎬 Content-Based Movie Recommendation System")
    print("Available movies:")
    for title in movie_titles:
        print(f"- {title}")

    movie = input("\nEnter a movie name from the list above: ")
    results = recommend(movie)

    if isinstance(results, str):
        print(results)
    else:
        print("\nRecommended movies:")
        for r in results:
            print(f"- {r}")
