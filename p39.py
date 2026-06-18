import streamlit as st
num1=st.number_input("enter no1")
num1=(int)(num1)
num2=st.number_input("enter no2")
num2=(int)(num2)
if st.button("click"):
    if num1>num2:
        st.write(num1,"is min")
    else:
        st.write(num2,"is min")
