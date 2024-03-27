import streamlit as st
import pandas as pd
import re
import json
import pandas as pd

def app():
    
    def clean_data(text):
        # Replace non-alphanumeric characters with spaces
        text = re.sub(r"[^a-zA-Z0-9\s]", " ", str(text))
        # Replace multiple spaces with single spaces
        text = re.sub(r"\s+", " ", text)
        # Remove leading and trailing spaces
        text = text.strip()
        
        return text
    
    def insert_sentence_to_jsonl(sentence, jsonl_file):
        # Load existing JSONL file
        try:
            with open(jsonl_file, 'r') as f:
                data = [json.loads(line.strip()) for line in f]
        except FileNotFoundError:
            data = []
        
        # Check for duplicates
        existing_texts = set(item["text"] for item in data)
        if sentence not in existing_texts:
            # Append new sentence to data
            data.append({"text": sentence})
        else:
            print("Duplicate sentence found. Appending to the last row.")
    
        # Write updated data to JSONL file
        with open(jsonl_file, 'w') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')
                
    def jsonl_to_csv(jsonl_file, csv_file):
        # Initialize an empty list to store the data
        data = []
    
        # Read the JSONL file
        with open(jsonl_file, 'r') as f:
            for line in f:
                # Parse each line as JSON
                json_data = json.loads(line)
                data.append(json_data)
    
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)
    
        # Write the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)

    def delete_last_row_from_jsonl(jsonl_file):
        # Read the existing JSONL file
        with open(jsonl_file, 'r') as f:
            lines = f.readlines()
    
        # Rewrite the file excluding the last line
        with open(jsonl_file, 'w') as f:
            for line in lines[:-1]:
                f.write(line)

    # Prompt user for a new sentence
    new_sentence = st.text_input("Enter a new sentence: ")
    
        
    # Clean the new sentence
    cleaned_sentence = clean_data(new_sentence)
    
    # Insert the cleaned sentence into the JSONL file
    insert_sentence_to_jsonl(cleaned_sentence, "AdsText.jsonl")
    
    jsonl_to_csv("AdsText.jsonl", "New.csv")

    df = pd.read_csv("New.csv")

    st.dataframe(df, width=700)

    if st.button("Delete"):
        delete_last_row_from_jsonl("AdsText.jsonl")
