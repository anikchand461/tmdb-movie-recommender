# 🎬 TMDB Movie Recommender

A web app built with **Streamlit** that gives movie recommendations using TMDB (The Movie Database) data.  
Combine data science, NLP, and machine learning to find films you’ll love.

---

## 🧩 Features

- Load and explore TMDB datasets (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`)  
- Preprocess movie titles, cast & crew data with NLP techniques  
- Compute similarity metrics (e.g. cosine similarity) for recommendations  
- Provide a simple UI where users input a movie and get similar titles  
- Interactive and visual outputs via Streamlit  

---

## 🗂 Repo Structure

├── app.py # Streamlit app script / entrypoint
├── main.ipynb # Notebook for analysis, prototyping, experiments
├── requirements.txt # Python dependencies
├── tmdb_5000_movies.csv # Main movie metadata dataset
├── tmdb_5000_credits.csv # Cast & crew information
└── README.md # This project documentation



---

## ⚙️ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/anikchand461/tmdb-movie-recommender.git
   cd tmdb-movie-recommender
   ```

2. **(Optional but recommended) Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate         # Windows
   ```

3. ** Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Run the project
```bash
streamlit run app.py
```


