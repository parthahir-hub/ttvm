import streamlit as st
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Home")

with col2:
    st.header("About")

with col3:
    st.header("Register")
st.image("https://s2.dmcdn.net/v/FmFY11epLVsE7Mqt2/x1080")
st.header("our story")
st.write("In a small village, there lived a curious boy named Aryan. He loved exploring old places and discovering forgotten things.")
st.write("One afternoon, while cleaning his grandfather's attic, Aryan found a dusty old clock. It was made of wood and had strange symbols carved around its face")
st.write("Grandpa, does this clock work? Aryan asked.")
st.write("His grandfather smiled.No one has been able to make it work for years.")
st.write("That night, Aryan carefully cleaned the clock and turned its rusty key. To his surprise, the clock began ticking.")
st.write("Tick... Tock... Tick... Tock...")
st.write("Suddenly, the room filled with a bright golden light. The hands of the clock started spinning backward.")
st.write("When the light disappeared, Aryan found himself standing in the same village—but everything looked different. The roads were made of dirt, there were no cars, and people wore old-fashioned clothes.")
st.write("I've traveled to the past! Aryan whispered.")
st.write("As he explored, he met a young boy who looked surprisingly familiar. The boy introduced himself as Ravi—the younger version of Aryan's grandfather.")
st.write("The two quickly became friends. Ravi showed Aryan around the village and told him about a treasure map hidden near the old banyan tree.")
st.write("together they searched for the treasure. After hours of digging, they found a small wooden chest. Inside were gold coins and a note:")
st.write("The greatest treasure is not gold but the memories you create with those you love.")
st.write("Before Aryan could say anything, the clock in his pocket began ticking loudly again.")
st.write("Tick... Tock... Tick... Tock...")
st.write("A bright light surrounded him, and he was pulled back to the attic.")
st.write("The next morning, Aryan ran to his grandfather and told him everything.")
st.write("His grandfather listened quietly and then smiled.")
st.write("From his pocket, he pulled out an old photograph. It showed a young Ravi standing beside a mysterious boy.")
st.write("That boy, Grandpa said, looks exactly like you.")
st.write("Aryan stared at the picture in amazement.")
st.write("The old clock never worked again, but Aryan kept it on his desk as a reminder that some treasures are worth more than gold—and some adventures are never forgotten.")
st.write("The End. 📖✨")
st.header("contact us")
col1,col2=st.columns(2)
with col1:
    st.text_input("name")
with col2:
    st.text_input("email")
    st.text_area("message")
    st.button("submit")

         
         
         



