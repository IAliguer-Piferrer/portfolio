#!/usr/bin/env python3
import os
import streamlit as st


if __name__ == "__main__":
    
    st.set_page_config(
        page_title="About Ignasi", 
        page_icon=":computer:", 
        layout="wide")
    
    st.image("assets/profile_picture.png", width="content")
    
    #st.title("Welcome to my personal website! :wave:")
    
    #st.write("This is my personal website where I share my career journey, projects, and insights. Feel free to explore and connect with me!")

    st.sidebar.success("Select a category to learn more about me!")

    st.markdown(
        """
        # Hello, I'm Ignasi :wave:

        I am a technology leader with a strong focus on building scalable, data-driven products. Over the past years, I have co-founded and led the engineering efforts at SAALG Geomechanics, where I designed and developed a cloud-based SaaS platform from the ground up, serving enterprise clients across industries.

        My work sits at the intersection of **software engineering, data, and AI**. I enjoy turning complex problems into practical, reliable solutions—whether that means designing system architectures, building full-stack applications, or experimenting with modern AI approaches such as LLMs, RAG systems, and agent-based workflows.

        I believe great software comes from **strong fundamentals, fast iteration, and close alignment with real user needs**. I enjoy working hands-on with code, leading teams from within, and creating environments where engineers can move quickly while maintaining high standards of quality and reliability.

        Outside of work, I value **health, sustainability, and continuous learning**—principles that also shape how I approach building products and teams.

        Feel free to explore my work, projects, and experiments below.

        -------------
         
        ### Want to learn more about me?

        - LinkedIn profile: [linkedin.com/in/ignasi-aliguer](https://www.linkedin.com/in/ignasi-aliguer)

        - GitHub: [github.com/ialiguer-piferrer](https://github.com/ialiguer-piferrer)
        
        """
        )

     