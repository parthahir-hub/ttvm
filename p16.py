import streamlit as st
st.header("image genrator")
q1=st.radio("select your image",["car","plane","sonic"])
if st.button ("submit"):
    if q1=="car":
        col1,col2,col3=st.columns(3)
        with col1:
            st.image("https://robbreport.com/wp-content/uploads/2020/06/lamborghini-centenario-roadster-1.jpg?w=1000")
        with col2:
            st.image("https://i.redd.it/yhb0u926jb381.jpg")
        with col3:
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnXb1jqWujyP7lmro5poVmxKniQoI2KcO7-g&s")
if q1=="plane":
    st.image("https://cdn.mos.cms.futurecdn.net/cLZzTWsjPLFizgw99mSJwK.jpg")
if q1=="sonic":
    st.image("https://m.media-amazon.com/images/I/51-CmSvI6DL._AC_UF894,1000_QL80_.jpg")                
