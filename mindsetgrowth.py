#streamlit
import streamlit as st
st.set_page_config(page_title= "Growth Project", page_icon="★")
st.title("Growth Mindset Challeng: Web App with Streamlit")
st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace Challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

#quote section
st.header("💡 Today,s Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. Winston Churchill")

st.header("🔧 What,s Your Challenge Today?")
user_input = st.text_input("Describe a  Challenge you,re facing:")

#condition
if user_input:
    st.success(f"You,re facting: {user_input}. Keep pushing forward towords your Goal!🚀")
else:
    st.warning("Tell us about Your Challenge to get Started!") 
   
#reflexing
st.header(" Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Gret insight! your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share ypur difficulties")

#acheivements
st.header("🏆 Celebrate Your Wins!")
acheivment =st.text_input("Share something you,ve recently accomplished:")

if acheivment:
    st.success(f"🌠 Amazing! you achieved: {acheivment}")
else:
    st.info("big or small , every acheivement counts! share one now 😍")    
#footer
st.write("- - -")
st.write("🚀 keep believing in yourself. growth is a journey, not a destination! 🌟")
st.write("**⛔ Created by Asma Muslim**")
