#!/usr/bin/env python3

import streamlit as st
import os
from model import call_rag_system
from dotenv import load_dotenv
load_dotenv()




if __name__ == "__main__":

    st.title("ASK ME ANYTHING! :speech_balloon:")
    st.write("Ask me anything about my career, experience, projects, or anything else you want to know! Just choose any sample question or type your question in the chat box below and hit enter.")
    
    questions = [
        "What is Ignasi Aliguer-Piferrer's current role and main responsibilities at SAALG ?",
        "Can you tell me about his experience prior to founding SAALG Geomechanics ?",
        "Has Ignasi Aliguer-Piferrer participated in any patents?"
    ]

    selected = st.pills("Sample Questions: ", questions, selection_mode="single")

    if selected:
        st.session_state["pending_prompt"] = selected
        
    
    user_question = st.chat_input("Ask me anything :")

    prompt = user_question or st.session_state.pop("pending_prompt", None)

    if prompt:
        with st.spinner("Searching for information ..."):
            answer = call_rag_system(prompt)
            st.write(answer)
    