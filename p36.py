import streamlit as st
num=st.number_input("enter no")
if st.button("click"):
    if  num>0:
        st.title("positive")
    elif num<0:
        st.title("nega")
    else:
         st.title("zero")              
