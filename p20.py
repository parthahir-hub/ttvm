import streamlit as st
import random
st.header("number gussing game")
number=st.number_input("enter number between 1to5")
if st.button("submit"):
    num=random.randint(1,5)
    if number==num:
        st.write("computer generate",num)
        st.success("successfuly done")
    else:    
        st.error("plese try again")


