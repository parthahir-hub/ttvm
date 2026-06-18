import streamlit as st
num1=st.number_input("enter nom1")
num1=(int)(num1)
num2=st.number_input("enter num2")
num2=(int)(num2)
if st.button("click"):
    if num1>num2:
        st.write(num1,"is max")
    else:
        st.write(num2,"is max")
