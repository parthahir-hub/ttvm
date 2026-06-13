import streamlit as st
import random
st.header("rock,paper,scisor game")
st.write("1.rock🗻🗻🗻 2.paper📄📄📄 3.scisor✂️✂️✂️")
bot=random.randint(1,3)

user=st.number_input("enter number from 1 to 3")
user=int(user)
if st.button("click"):
    if bot==user:
        st.title("match withdraw")
        st.write("computer choose",bot)
        st.write("you choose",user)
    elif ((user==1 and bot==3)or (user==2 and bot==1)or (user==3 and bot==2)):
        st.write("you win")
        st.balloons()
        st.write("computer chose",bot)
        st.write("you chose",user)
    else:
        st.write("computer wins")
        st.write("computer chose",bot)
        st.write("you chose",user)
        st.snow()