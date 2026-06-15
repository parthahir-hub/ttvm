import streamlit as st
num=st.number_input("enter no")
num=(int)(num)
if st.button("click"):
    for i in range(1,num+1):
        if i==1:
         st.write("😀")
        elif i==2:
            st.write("😊")
        elif i==3:
            st.write("🥱")
        elif i==4:
            st.write("💩")
        elif i==5:
            st.write("😈")
        elif i==6:
            st.write("😇")
        elif i==7:
            st.write("🤪")
        elif i==8:
            st.write("🥳")
        elif i==9:
            st.write("🥶")
        elif i==10:
            st.write("🤑")                                

