import streamlit as st
num=st.number_input("enter age")
if st.button("click"):
    if num>=18:
        st.title("you are aligable for vote")
    if num<18:
        st.title("you are not aligable for given vote")    