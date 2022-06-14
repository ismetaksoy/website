import streamlit as st

# Page settings
st.set_page_config(page_title='PTP Ismet Aksoy', 
                    page_icon=None, layout="wide", initial_sidebar_state="auto", 
                    menu_items={
                        'Get Help': 'https://www.extremelycoolapp.com/help',
                        'Report a bug': "https://www.extremelycoolapp.com/bug",
                        'About': "# This is a header. This is an *extremely* cool app!"
                    })

st.header('Ismet Aksoy')
st.subheader('About me')
st.write('''
:star: Ambitious :moon: Creative :smile: Hardworking

That's how I would describe myself
''')

st.subheader('Work')
st.write('''<p>
Experienced individual currently working as a Business Intelligence Consultant for the Healthcare
sector. We try to improve the healthcare sector by making data usefull.
My current responsiblities are:
<li>Creating Dashboards</li>
<li>Providing support to our customers</li>
<li>Writing complex SQL queries to adjust the datamodel</li>
<li>Documenting the requests of the users in Functional Design Documents and discuss this further to uncover
the need of the user</li>
<li>Assisting the Product Owner</li>

In my professional career I focus on three key aspects
</p>
''', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<h3> Process </h3>', unsafe_allow_html=True)
    st.markdown('''<p>
                Process are the steps that we define and need to take in order to achieve our goals
                </p>''', unsafe_allow_html=True)
with col2:
    st.markdown('<h3> Technology </h3>', unsafe_allow_html=True)
    st.markdown('''<p>
                Technology is what we use to achieve our goals
                </p>''', unsafe_allow_html=True)
with col3:
    st.markdown('<h3> Personality </h3>', unsafe_allow_html=True)
    st.markdown('''<p>
                Personality is 
                </p>''', unsafe_allow_html=True)