import streamlit as st
num=st.number_input("enter number")
num=(int)(num)
if st.button("click"):
    for i in range(1,num+1):
        st.write(i)

