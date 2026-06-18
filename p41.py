import streamlit as st
st.header("ractangle area")
num1=st.number_input("enter length")
num1=(int)(num1)
num2=st.number_input("enter width")
if st.button("click"):
    a=num1*num2
    st.write(a)