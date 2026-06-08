import streamlit as st
import random

st.title("Random Number Generator")

if st.button("Generate"):
    num=random.randint(1,100)
    st.write("Random Number:", num)
    
