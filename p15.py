import streamlit as st
st.header(" mood generate emojis")
q1=st.radio("select your mood",["happy","sad","surprise","Bored"])
if st.button("submit"):
    if q1=="happy":
        st.header("🌝")
    if q1=="sad":
        st.header("🙁")
    if q1=="surprise":
        st.header("😲")
    if q1=="Bored" :
        st.header("😒")
          