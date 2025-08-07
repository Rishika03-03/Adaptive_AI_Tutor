#Road map using AI agent gemini

import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY="AIzaSyCA2wJvuDAH5keV6Zcnfr3wZVwwowNDsdUAIzaSyD4_oZYY9CM3Yi-ZnSTdoHEDlKp3b8Qcks"
genai.configure(api_key=GEMINI_API_KEY)

def generate_prompt(subject,year,speed,goal):
  prompt=f"""Structured road map for students in {subject}
  and provide a {year} the student is learner {speed}
  his aim is to achieve {goal}
  -topics
  -leetcode Questions
  -youtube links

  ** Format as a table **
  Day | Topics | Leetcode Questions | Youtube Links 
  """
  
  model=genai.GenerativeModel("gemini-2.0-flash-exp")
  response=model.generate_content(prompt)
  return response.text
st.title("Personalized RoadMap")
subject=st.selectbox("Please choose Subject",["Artificial Intelligence","Machine Learning","Cyber Security","Data Analytics"])
year=st.selectbox("Choose year",["1","2","3","4"])
speed=st.radio("Learning Speed",["Slow","Medium","Fast"])
goal=st.selectbox("Pick the Goal",["Master the subject to the core","Learn just basics","To learn core cyber security"])
date_range=st.date_input("select a date range",[])
if st.button("Generate Roadmap"):
  with st.spinner("Generating your roadmap..."):
    prompt_text=generate_prompt(subject,year,speed,goal)

