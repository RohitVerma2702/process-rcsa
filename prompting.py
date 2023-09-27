import os
import openai
import toml
import streamlit as st

secrets = toml.load("secrets.toml")
openai.api_key = secrets["openai_api_key"]

# openai.api_key = st.secrets["openai_api_key"]

def generate_risks(process, num_risks, risk_category):
    # Define your JSON format separately
    json_format = '''
    {
        "Risks": [
            {
                "Risk Title": "Title of Risk 1",
                "Risk Category": "Category of Risk 1"
            },
            {
                "Risk Title": "Title of Risk 2",
                "Risk Category": "Category of Risk 2"
            },
            {
                "Risk Title": "Title of Risk 3",
                "Risk Category": "Category of Risk 3"
            },
            {
                "Risk Title": "Title of Risk 4",
                "Risk Category": "Category of Risk 4"
            },
            {
                "Risk Title": "Title of Risk 5",
                "Risk Category": "Category of Risk 5"
            },
            {
                "Risk Title": "Title of Risk 6",
                "Risk Category": "Category of Risk 6"
            }
        ]
    }
    '''

    # Use the JSON format variable in your risk_titles string
    risk_titles = f"""As an Operational Risk expert, please provide {num_risks} risks associated with the process of {process}. Categorize these risks into the following {risk_category}.

    Present the information in the following JSON format:
    {json_format}

    Ensure that each risk title contains 8 to 15 words and always includes a word associated with a threat or negative event. Take your time to consider and provide an appropriate response, and include only the risk titles and categories in your answer."""


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": risk_titles}],
        temperature=1,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response

def generate_risk_information(risk_title, risk_category_name):

    text = f"""
    Imagine you are an Operational Risk expert.
    Generate risk information for "{risk_title}" in the following format:

    1. Risk Title: The number of words in the risk title should be between 8 to 15 words and should always contain a word associated with threat or a negative event.
    2. Description: Provide a detailed description between 30 to 75 words. Description should contain details of how the risk can occur.
    3. Causes: List the key causes as bullet points.
    4. Financial Impacts: List the key financial impacts as bullet points.
    5. Non-Financial Impacts: List the key non-financial impacts as bullet points.
    6. Banking Example: Provide 1 example of how this risk can occur in a bank.
    7. Risk Category: Should be one or more from the values: {risk_category_name}.

    Please use this information to construct an HTML table row in the following format:

    <tr>
        <td>"Risk Title"</td>
        <td>"Description"</td>
        <td>"Causes"</td>
        <!-- Add more <td> elements for Financial Impacts, Non-Financial Impacts, Banking Example, and Risk Category -->
    </tr>

    Please take your time to generate the information and make sure to only provide the HTML code with no additional information.
    """

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
