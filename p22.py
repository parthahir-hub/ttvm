import streamlit as st
num=st.number_input("enter number")
if st.button("submit"):
    if num==1:
        st.write("January")
    if num==2:
        st.write("February")
    if num==3:
        st.write("March")
    if num==4:
        st.write("April")
    if num==5:
        st.write("May")
    if num==6:
        st.write("June")                
    if num==7:
        st.write("July")
    if num==8:
        st.write("August")
    if num==9:
        st.write("September")
    if num==10:
        st.write("October")
    if num==11:
        st.write("November")
    if num==12:
        st.write("December")
                    