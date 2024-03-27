import streamlit as st

def app():
    st.title(':red[SENHENG] Text Generator')
    
    st.markdown(st.session_state["Mistral_bot_response"])
