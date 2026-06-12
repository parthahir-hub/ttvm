import streamlit as st
import random
st.header("rock,paper,scissor🎮")
st.write("1.rock⛰️⛰️⛰️⛰️ 2.paper📃📃📃📃📃  3.scissors✂️✂️✂️✂️")
num=random.randint(1,3)

no=st.number_input("enter no 1 to 3")
if st.button("click"):
    if no==num:
        st.title("match withdraw")
        st.write("computer choose",num)
        st.write("you choose",no)
    elif ((no == 1 and num == 3) or ( no== 2 and num == 1) or (no == 3 and num == 2)):
        st.title("you win🕵️‍♂️🕵️‍♂️🕵️‍♂️🕵️‍♂️🕵️‍♂️🕵️‍♂️")
        st.balloons()
        st.write("computer choose",num)
        st.write("you choose",no)
    else:
        st.title("computer win🖥️🖥️🖥️🖥️🖥️🖥️")
        st.write("computer choose",num)
        st.write("you choose",no)
        st.snow()
