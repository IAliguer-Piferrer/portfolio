#!/usr/bin/env python3

import streamlit as st
import os
from model import call_rag_system
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":
    
    st.title("ASK ME ANYTHING! :speech_balloon:")
    st.write("Ask me anything about my career, experience, projects, or anything else you want to know! I will do my best to answer based on the information I have available. Just type your question in the chat box below and hit enter.")
    
    questions = [
        "What is Ignasi Aliguer-Piferrer's current role and what are your main responsibilities?",
        "Can you tell me about your experience at SAALG Geomechanics?",
        "Has Ignasi Aliguer-Piferrer participated in any patents?"
    ]

    selected = st.pills("Sample Questions: ", questions, selection_mode="single")

    if selected:
        st.session_state["pending_prompt"] = selected
        
    # st.markdown("""
    #             - What is Ignasi Aliguer-Piferrer's current role and what are your main responsibilities?

    #             - Can you tell me about your experience at SAALG Geomechanics?",
                
    #             - Has Ignasi Aliguer-Piferrer participated in any patents? 
    #             """)

    
    user_question = st.chat_input("Ask me anything :")

    prompt = user_question or st.session_state.pop("pending_prompt", None)

    if prompt:
        with st.spinner("Searching for information ..."):
            answer = call_rag_system(prompt)
            st.write(answer)
    