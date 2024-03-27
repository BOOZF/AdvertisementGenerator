import streamlit as st

## Mistral Library
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from transformers import BitsAndBytesConfig

def call_mistral():

    model_id = "BOO0710/Mistral7B"

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    pipe = pipeline(
        "text-generation", 
        model=model_id, 
        tokenizer = tokenizer, 
        max_length = 300
    )
    
    return pipe

def GenerateMISTRAL(query):
    
    pipe = call_mistral()
    
    hf = HuggingFacePipeline(pipeline=pipe)
    
    prompt = f"<s>[INST]Provide me Senheng advertisment text with keywords: ({query})[/INST]"
    
    response = hf(prompt)
    
    return response

def call_llama2():

    model_id2 = "Chinxian1121/LLama2BLora"

    tokenizer2 = AutoTokenizer.from_pretrained(model_id2)
    pipellama = pipeline(task="text-generation", model=model_id2, tokenizer=tokenizer2, max_length=300)

    return pipellama

def Llama2_generator(query):

    pipellama = call_llama2()
    
    # Form the prompt by concatenating the user's keywords with the prefix
    prompt = f"<s>[INST]Provide me 5 advertisement taglines with keywords: ({query})[/INST]"
    
    # Generate the text
    result = pipellama(prompt)
    
    # Extract the generated text from the result
    generated_text = result[0]['generated_text']
    
    # Remove the keyword from the generated text
    generated_text_without_keyword = generated_text.replace(prompt, "")
    
    # Print the generated text without the keyword
    return generated_text_without_keyword

def app():
    if "Mistral_bot_response" not in st.session_state:
            st.session_state["Mistral_bot_response"] = ""
    
    if "LLama2_bot_response" not in st.session_state:
            st.session_state["LLama2_bot_response"] = ""
    
    Mistral_bot_response = ""
    LLama2_bot_response = ""
    done = ""
    
    st.title(':red[SENHENG] Text Generator')
       # Get user input
    user_input = st.text_area("Enter the advertisement keywords: ", height=20, key="input")
    if st.button("Send"):
        # Check for exit command
        if user_input.lower() == 'exit':
            st.markdown("<h3 style='text-align: left; font-family: Courier New;'>Goodbye!</h3>", unsafe_allow_html=True)
        else: 
            # Generate response
            Mistral_bot_response = GenerateMISTRAL(user_input)
            
            if Mistral_bot_response == "":
                st.markdown("<h3 style='text-align: left; font-family: Courier New;'>Loading。。。。。</h3>", unsafe_allow_html=True)
            else:
                st.session_state["Mistral_bot_response"] = Mistral_bot_response
                done = "Successfully DONE !"

                # Generate response from Llama2 model
                LLama2_bot_response = Llama2_generator(user_input)
                if LLama2_bot_response == "":
                    st.markdown("<h3 style='text-align: left; font-family: Courier New;'>Loading Llama2 response...</h3>", unsafe_allow_html=True)
                else:
                    st.session_state["LLama2_bot_response"] = LLama2_bot_response
    
    st.markdown("<p style='text-align: left; font-family: Times New Roman; font-size: 18px;'>" + done + "</p>", unsafe_allow_html=True)