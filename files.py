import streamlit as st
import pandas as pd
st.subheader("Loading the CSV File")

df = st.file_uploader("Upload the CSV File: ", type = ['csv', 'xlsx'])
df = pd.read_csv('Products.csv')

if df is not None:
    st.table(df.head())

st.subheader('Dealing with Images')
st.image('img.png')

st.subheader('Dealing with Images while uploading')
img_file = st.file_uploader("Upload the Image file : ", type = ['png', 'jpeg'])
if img_file is not None:
    st.image(img_file)

st.subheader('Working with Videos')
video_file = st.file_uploader("Upload the Video file : ", type = ['mkv', 'mp4'])
if video_file is not None:
    st.video(video_file.read(), start_time = 2)


st.subheader('Working with Audio')
audio_file = st.file_uploader("Upload the Audio file : ", type = ['wav', 'mp3'])
if audio_file is not None:
    st.audio(audio_file.read(), start_time = 2)





