import streamlit as st
import json
import pandas as pd
from bs4 import BeautifulSoup
import prompting
from PIL import Image
import streamlit.components.v1 as components

im = Image.open("./assets/images/RS-square-logo.jpeg")

st.set_page_config(
    layout="wide", page_title="RiskSpotlight - Process RCSA", page_icon=im
)

hide_streamlit_style = """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Process RCSA - Risk Identification")

col1, col2 = st.columns(2)

with col1:
    process = st.text_area("Please provide Process details.", value="", height=200)
    clicked = st.button("Submit")

with col2:
    num_risks = st.number_input(
        "Number of Risks...", min_value=3, max_value=10
    )
    risk_category = st.multiselect(
        "Please select Risk Categories.",
        ["Business Process Execution Failures", 
        "Damage to Tangible and Intangible Assets",
        "Employment Practices and Workplace Safety",
        "External Theft & Fraud",
        "Improper Business Practices",
        "Internal Theft & Fraud",
        "Regulatory & Compliance",
        "Technology Failures & Damages",
        "Vendor Failures & Damages"],
    )

if clicked:
    if not process or not num_risks or not risk_category:
        st.sidebar.warning("Please fill in all the information.")

    else:
        with st.spinner("Please wait..."):
            response = prompting.generate_risks(process, num_risks, risk_category)

            risks_output = response["choices"][0]["message"]["content"]

            # Parse the JSON response
            data = json.loads(risks_output)
            # st.write(risks)
            # st.write(data)

            # Iterate through the extracted data
            risks = data["Risks"]

            risk_table_rows = ""

            for risk in risks:
                risk_title = risk["Risk Title"]
                risk_category_name = risk["Risk Category"]

                final_response = prompting.generate_risk_information(risk_title, risk_category_name)

                risk_table = final_response["choices"][0]["message"]["content"]

                risk_table_rows = risk_table_rows + risk_table

            html_before = """
            <table>
                <tr style="background-color: #000; color: #fff; text-align: center;">
                    <th>Risk Title</th>
                    <th>Description</th>
                    <th>Causes</th>
                    <th>Financial Impacts</th>
                    <th>Non-Financial Impacts</th>
                    <th>Banking Example</th>
                    <th>Risk Category</th>
                </tr>
            """

            html_after = """
            </table>
            """

            # Concatenate everything together
            final_html = html_before + risk_table_rows + html_after

            # Display the HTML table
            st.write(final_html, unsafe_allow_html=True)