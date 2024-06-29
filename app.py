import pickle
import streamlit as st
import pandas as pd
import requests

#importing data
movies_dict=pickle.load(open('moviesdict.pkl', 'rb'))
df=pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

#to fetch movie titles and display it on localhost
selected_movie_name = st.selectbox(
'Please tell your favourite movie name',
    (df['title'].values))

#to fetch similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

#function to recommend top 5 similar movies
def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
                  1:6]  # sorting the recommendations by similarity

    recommended_movies = [] #to store recommended movies
    recommended_movies_posters = []
    for i in movies_list:
        movie_id=df.iloc[i[0]].movie_id #contains the movie id in dataframe
        #fetch poster from api

        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(df.iloc[i[0]].title)
    return recommended_movies, recommended_movies_posters


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c3643366335c241ae50ae3c45b2582d1'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

if st.button('Recommend similar movies'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0])
        st.image(posters[0])

    with col2:
        st.header(names[1])
        st.image(posters[1])

    with col3:
        st.header(names[2])
        st.image(posters[2])

    with col4:
        st.header(names[3])
        st.image(posters[3])

    with col5:
        st.header(names[4])
        st.image(posters[4])