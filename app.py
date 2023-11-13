import pickle

import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
#FOR GETTING POSTER OF THE MOVIE FROM API DATABASE WITH HALF API PATH AND FULL API PATH
    return full_path

#recommend fun WE HAVE USED IN SORCE CODE
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True , key = lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster =[]
    for i in distance[1:6]:   # how many similar movies u want to
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name,recommended_movies_poster




st.header("Movie Recommendation System using ML")


# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movies_name,recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])

        # Footer or Tail
# Add a placeholder for the footer to push it to the bottom of the page
st.markdown('<div style="height: 400px;"></div>', unsafe_allow_html=True)

# Footer with your name at the bottom right corner
footer = """
<footer style="position: absolute; bottom: 0; right: 0; text-align: right; padding: 10px;">
 Done by siva and Vinay
</footer>
"""

st.markdown(footer, unsafe_allow_html=True)



