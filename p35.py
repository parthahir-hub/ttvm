import streamlit as st
num=st.number_input("enter no")
num=(int)(num)
if st.button("click"):
    if num%2==0:
        st.title("no is even")
    else:
        st.title("no is odd")
