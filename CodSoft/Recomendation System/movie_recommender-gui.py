import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import ttk, scrolledtext

# -------------------------------
# 🎬 Movie Dataset
# -------------------------------
data = {
    'title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Prestige',
        'The Dark Knight', 'Memento', 'Tenet', 'Avatar', 'Titanic', 'The Martian'
    ],
    'genre': [
        'Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Drama',
        'Action', 'Thriller', 'Sci-Fi', 'Fantasy', 'Romance', 'Sci-Fi'
    ],
    'description': [
        'A computer hacker learns about the true nature of reality and his role in the war against its controllers.',
        'A thief who steals corporate secrets through dream-sharing technology is given a chance to erase his criminal past.',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity’s survival.',
        'Two magicians engage in a battle to create the ultimate illusion while sacrificing everything they have.',
        'Batman faces the Joker, a criminal mastermind who plunges Gotham into chaos.',
        'A man with short-term memory loss uses notes and tattoos to hunt for his wife’s killer.',
        'A secret agent embarks on a time-bending mission to prevent World War III.',
        'A paraplegic marine dispatched to the moon Pandora becomes torn between following orders and protecting the world he feels is his home.',
        'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious Titanic.',
        'An astronaut becomes stranded on Mars and must rely on his ingenuity to survive.'
    ]
}

df = pd.DataFrame(data)
df['combined_features'] = df['genre'] + " " + df['description']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation Function
def recommend(title, df=df, similarity=cosine_sim, top_n=5):
    if title not in df['title'].values:
        return ["❌ Movie not found in database."]
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    recommended = df.iloc[[i[0] for i in sim_scores]][['title', 'genre']]
    return [f"{row['title']} ({row['genre']})" for _, row in recommended.iterrows()]

# -------------------------------
# 🖼️ GUI Setup
# -------------------------------
def show_recommendations():
    selected_movie = movie_var.get()
    results = recommend(selected_movie)
    output_box.config(state='normal')
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, f"\n🎬 Because you liked '{selected_movie}', you might also enjoy:\n\n")
    for rec in results:
        output_box.insert(tk.END, f"- {rec}\n")
    output_box.config(state='disabled')

root = tk.Tk()
root.title("🎬 Movie Recommendation System")
root.geometry("500x400")
root.resizable(False, False)

# Dropdown
movie_var = tk.StringVar()
movie_dropdown = ttk.Combobox(root, textvariable=movie_var, values=list(df['title']), font=("Arial", 12), state="readonly")
movie_dropdown.set("Select a movie")
movie_dropdown.pack(pady=10)

# Button
recommend_button = tk.Button(root, text="Get Recommendations", command=show_recommendations, font=("Arial", 12))
recommend_button.pack(pady=5)

# Output Box
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 11), height=15, width=60)
output_box.pack(padx=10, pady=10)
output_box.config(state='disabled')

root.mainloop()