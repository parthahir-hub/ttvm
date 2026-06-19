import streamlit as st
st.header("area calculation app")
st.title("rectangle area")
num1=st.number_input("enter length")
num1=(int)(num1)
num2=st.number_input("enter width")
num2=(int)(num2)
if st.button("rectangle"):
    area=num*num2
    st.write(a)
st.title("sqare area")

num3=st.number_input("enter length1")
num3=(int)(num3)
if st.button("sqare"):
    a=num3*num3
    st.write(a)
st.title("circle area")

num4=st.number_input("enter radius")
num4=(int)(num4)
if st.button("circle"):
    area=3.14*num4*num4
    st.write(a)        