import streamlit as st

def app():
    st.title(':red[SENHENG] Text Generator')
    
    st.markdown(st.session_state["LLama2_bot_response"])