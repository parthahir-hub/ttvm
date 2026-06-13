import streamlit as st
st.header("factorial")
num=st.number_input("enter no")
num=(int)(num)
if st.button("click"):
    f=1
    for i in range(1,num+1):
        f=f*i
    st.write(f)    