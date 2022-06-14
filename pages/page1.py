import streamlit as st
#from streamlit_app import name, account_number


account_number = st.text_input('Account Number', 
                                key = 'account_number', 
                                value = st.session_state['account_number'] if 'account_number' in st.session_state else '')


(st.session_state)