import streamlit as st
st.header("cirle area")
num=st.number_input("enter radius")
num=(int)(num)
if st.button("click"):
    a=3.14*num*num
    st.title(a)