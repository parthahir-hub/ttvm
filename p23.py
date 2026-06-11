import streamlit as st
import random
st.header("rock,paper, Scissors")
st.write("1.rock 2.paper  3.scissors")
num=random.randint(1,3)

no=st.number_input("enter no 1 to 4 ")
if st.button("click"):
    if num==no:
        st.write("match withdraw")
        st.write("computer choose",num)
        st.write("you choose",no)
    elif ((no == 1 and num == 3) or ( no== 2 and num == 1) or (no == 3 and num == 2)):
        st.write("you win")
        st.write("computer choose",num)
        st.write("you choose",no)
    else:
        st.write("computer win")
        st.write("computer choose",num)
        st.write("you choose",no)


