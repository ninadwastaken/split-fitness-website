import streamlit as st

st.set_page_config(layout='wide')


# st.header("Split Fitness")
st.markdown("<h1 style='text-align: center; color: white;'>Split Fitness</h1>", unsafe_allow_html=True)

st.info("the only fitness app you'll ever need.")


import pandas

st.header("Features")

col1, col2 = st.columns(2)

df = pandas.read_csv("Fitness_App_Features.csv", sep=";")

print(df)

with col1:
    for idx, row in df[1::2].iterrows():
        ft, desc, img = row
        st.subheader(ft)
        st.info(desc)
        st.image(f'images/{img}')

with col2:
    for idx, row in df[2::2].iterrows():
        ft, desc, img = row
        st.subheader(ft)
        st.info(desc)
        st.image(f'images/{img}')


