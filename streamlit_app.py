import streamlit as st



text = st.write('Homepage')




name = st.text_input('What is your name?', key = 'name', value = st.session_state['name'] if 'name' in st.session_state else '')

st.write(st.session_state)