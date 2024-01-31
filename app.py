import streamlit as st

st.set_page_config(page_title='Información Jhon',page_icon='👨‍💻',layout='wide')


st.header('Jhon Kerly Mosquera Información previa a entrevista 👨‍💻')

col2,col3=st.columns(2)

with col2:
    st.video('videos/20240131 141446.mp4')
with col3:
    st.video('videos/video.mp4')

col,col1=st.columns(2)

with col:
    st.link_button(label='call-center',url='https://call-center-dataset-jhon.streamlit.app/')

with col1:
    st.link_button(label='costumer',url='https://costumer-jb7mpmynfrbpw7ayujy3y3.streamlit.app/')