import streamlit as st
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

            st.header(process)
            risks = response["choices"][0]["message"]["content"]
            st.write(risks, unsafe_allow_html=True)
