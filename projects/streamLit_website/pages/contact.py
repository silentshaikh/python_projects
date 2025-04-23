import streamlit as st
import pandas as pd
import numpy as np
import re;

st.set_page_config(
    page_title="Portfolio - Contact",
    page_icon="🧑‍💻",
    layout="wide"
)
with st.sidebar:
    st.image("a.webp", width=200)

st.markdown(f"""
            <h1 style="color: #5EEAD4; font-family:'Courier New', Courier, monospace;">
           📧 Contact With Us
            </h1>
            """, unsafe_allow_html=True)

formError = {} # Errors of submited fomr      
with st.form("contact_form"):

   userName= st.text_input(label="User Name",placeholder="Enter You Name",)
   userEmail = st.text_input(label="User Email",placeholder="Enter You Email",)
   userNumber = st.text_input(label="User Number",placeholder="Enter You Number",)
   userGender = st.radio(label="Gender",options=["Male","Female"],)
   userMessage = st.text_area(label="User Message",placeholder="Enter Your Query",height=200,)
   formSubmit = st.form_submit_button("🚀 Submit")
   if formSubmit:
    if not userName:
        formError["userName"] = "❌ Name is Required"
    if not userEmail or not re.match(r"^[a-zA-Z0-9\_\.\%\+\-]+\@[a-zA-Z0-9\.\-]+\.[a-z]{2,7}$",userEmail):
        formError["userEmail"] = "❌ Enter a valid email"
    if not userNumber or not userNumber.isdigit() or len(userNumber)<11:
        formError["userNumber"] = "❌ Enter a valid phone number (10+ digits)."
    if not userMessage:
        formError["userMessage"] = "❌ Please Enter your Message"

    # Print Errors
    if formError:
        for fields, errorMsg in formError.items():
            st.error(errorMsg)
    else:
        st.success(f"Dear {userName}, ✅ Your Form has Submitted Successfully !")        

