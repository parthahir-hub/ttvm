import streamlit as st
st.number_input("enter no")
col1,col2,col3,col4=st.columns(4)
with col1:
    st.button("ce")
with col2:
    st.button("c")
with col3:
    st.button("🔙")
with col4:
    st.button("/")
col5,col6,col7,col8=st.columns(4)
with col5:
    st.button("7")
with col6:
    st.button("8")
with col7:
    st.button("9")
with col8:
    st.button("*")
col9,col10,col11,col12=st.columns(4)
with col9:
    st.button("4")
with col10:
    st.button("5")
with col11:
    st.button("6")
with col12:
    st.button("-")
col13,col14,col15,col16=st.columns(4)
with col13:
    st.button("1")
with col14:
    st.button("2")
with col15:
    st.button("3")
with col16:
    st.button("+")
col17,col18,col19,col20=st.columns(4)                
with col17:
    st.button("negate(")
with col18:
    st.button("0")
with col19:
    st.button(".")
with col20:
    st.button("=")                    