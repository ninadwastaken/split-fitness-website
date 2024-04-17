import streamlit as st

st.title("We are Split Fitness.")


c1, _, c2, _, c3 = st.columns(5)

with c1:
    st.header("Karan Pandey")
    st.link_button(url="https://www.linkedin.com/in/karan-pandey-079308252/", label="linkedin")

with c2:
    st.header("Ninad Moharir")
    st.link_button(url="https://www.linkedin.com/in/ninad-moharir", label="linkedin")

with c3:
    st.header("Pranav Penmatcha")
    st.link_button(url="https://www.linkedin.com/in/pranav-penmatcha/", label="linkedin")
