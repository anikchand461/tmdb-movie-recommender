import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import gdown

# Load environment variables
load_dotenv()
API_KEY = os.getenv('TMDB_API_KEY')

# Google Drive helper
def download_from_drive(file_id, dest_path):
    """Download a file from Google Drive if not already present."""
    if not os.path.exists(dest_path):
        st.write(f"Downloading {dest_path} from Google Drive...")
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, dest_path, quiet=False)

# File IDs
SIMILARITY_FILE_ID = "1CrOPF4OVR2eF_eph4YWOJN1zC_4aj6kM"
MOVIE_DICT_FILE_ID = "1pakuyxWz2ZEEnR6X4vwz9r7vBFgki68D"

# Ensure files are available
download_from_drive(SIMILARITY_FILE_ID, "similarity.pkl")
download_from_drive(MOVIE_DICT_FILE_ID, "movie_dict.pkl")

# Load data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

# Fetch poster
def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Recommender function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_posters = []
    recommended_links = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id   
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        recommended_links.append(f"https://www.themoviedb.org/movie/{movie_id}")
    
    return recommended_movies, recommended_posters, recommended_links

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'What movie do you want to watch?',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters, links = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.markdown(
                f"[![{names[idx]}]({posters[idx]})]({links[idx]})",
                unsafe_allow_html=True
            )
