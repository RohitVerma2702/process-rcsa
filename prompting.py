import os
import openai
import toml
import streamlit as st

# secrets = toml.load("secrets.toml")
# openai.api_key = secrets["openai_api_key"]

openai.api_key = st.secrets["openai_api_key"]


def generate_risks(process, num_risks, risk_category):
    text = f"""Imagine you are an Operational Risk expert.
    Please suggest me {num_risks} Risks for the following process:
    Proceess Detail: "{process}"
    The risks that you will provide should belong to the following Risk Categories:
    Risk Categories: {risk_category}.
    Please provide the output in an html table with the following information columns:
    1. Risk Title: The number of words in the risk title should be between 8 to 15 words and should always contain a word associated with threat or a negative event
    2. Description: Provide a detailed description between 30 to 75 words. Description should contain details of the how the risk can occur. 
    3. Causes: List the key causes as bullet points
    4. Financial Impacts: List the key financial impacts as bullet points
    5. Non-Financial Impacts: List the key non-financial impacts as bullet points
    6. Banking Example: Provide 1 example of how this risk can occur in a bank. 
    7. Loss Event Example: Provide 1 real-life example of a loss event that has occurred at another bank related to the risk. 
    8. Risk Category: Should be one or more from the values provided above.
    Please style the table header with black background, white font color and center aligned text. Please take you time to think and provide an appropriate response and make sure to only provide the html table and no other additional information."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=1,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response
