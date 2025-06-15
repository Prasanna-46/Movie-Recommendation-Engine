# Movie Recommendation Engine 🎬

This project implements a **content-based movie recommendation system** using Python. It analyzes textual metadata such as genres, cast, crew, and keywords to recommend movies that are similar in content.

## Features

- Extracts and combines movie metadata into a unified textual format
- Vectorizes metadata using `CountVectorizer`
- Computes similarity between movies using cosine similarity
- Recommends top N similar movies based on user input

## Tech Stack

- **Language**: Python
- **Libraries**: pandas, numpy, scikit-learn
- **Notebook**: Jupyter (.ipynb)
- **Dataset**: CSV file containing metadata for 4,800+ movies


## How It Works

1. **Data Preprocessing**: Extract relevant fields (title, genres, keywords, cast, crew).
2. **Feature Engineering**: Combine fields into a single string per movie.
3. **Vectorization**: Convert text to numeric vectors using `CountVectorizer`.
4. **Similarity Computation**: Calculate pairwise cosine similarity.
5. **Recommendation Function**: Returns the most similar movies for any given title.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Prasanna-46/Movie-Recommendation-Engine.git
cd Movie-Recommendation-Engine

2. Install required libraries:

pip install pandas scikit-learn numpy

3. Open the Notebook:

jupyter notebook Movie_Recommendation_Engine.ipynb
