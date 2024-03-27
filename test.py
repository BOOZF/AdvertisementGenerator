import streamlit as st
from streamlit_option_menu import option_menu
import home, newdata, social, tagline
   
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:
            #st.title(':red[SENHENG] Text Generator')
            selected = option_menu(
                menu_title= None,  # required
                options=["Home", "Social Text", "Tagline", "Datasets"],  # required
                icons=["house","house", "book", "file-bar-graph"],  # optional
                menu_icon= "cast",  # optional
                default_index=0,  # optional
            )
        
        #nav choices                        
        if selected == "Home":
            home.app()
                    
        if selected == "Social Text":
            social.app()
            
        if selected == "Tagline":
            tagline.app()
            
        if selected == "Datasets":
            newdata.app()
        

    run()