import requests
import streamlit as st
import pickle
import pandas as pd

movies=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies)

similarity_score=pickle.load(open('similarty_score.pkl','rb'))
# create Recommended moive main function
def movie_recommend(movie):
    moive_index=movies[movies['title']==movie].index[0]
    Recommended_moive=sorted(enumerate(similarity_score[moive_index]),reverse=True,key=lambda x:x[1])[0:4]
    recommend_movie=[]
    recommend_movie_poster =[]
    for i in Recommended_moive:

        recommend_movie.append(movies['title'][i[0]])
        #fetch Poster through API
        movie_id=movies['id'][i[0]]
        recommend_movie_poster.append(poster_fetch(movie_id))
    return recommend_movie,recommend_movie_poster
def poster_fetch(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=19555e7a04d80b513cb4faa0758d9a75'.format(movie_id))
    moives_data=response.json()
    return 'https://image.tmdb.org/t/p/original'+moives_data['poster_path']



st.title('Movie Recommender System')
option = st.selectbox(label="Please select the Moive which you want see",options=(movies['title'].values))
if st.button("recommend"):
    movie_name,poster=movie_recommend(option)
    col1, col2, col3,col4= st.columns(4)
    with col1:
        st.text(movie_name[0])
        st.image(poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(poster[3])
