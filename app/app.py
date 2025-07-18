import streamlit as st
import pickle as pkl
import pandas as pd
import requests
import os

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=1df0f5c9c8104027bec28c711ce22946&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pkl.load(open(os.path.join("model","movies_dict.pkl"),'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pkl.load(open(os.path.join("model","similarity.pkl"),'rb'))

st.title("Movie Recommender System")

selected_movies_name = st.selectbox(
    "Select a movie",
    movies['title'].values,
)

if st.button("Recommend"):
    names, posters = recommend(selected_movies_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])