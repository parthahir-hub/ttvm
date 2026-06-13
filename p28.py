import streamlit as st
st.header("sum of input number")
num=st.number_input("enter no")
num=(int)(num)
if st.button("click"):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    st.write(sum)