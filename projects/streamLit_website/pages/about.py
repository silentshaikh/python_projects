import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Portfolio - About",
    page_icon="🧑‍💻",
    layout="wide"
)

with st.sidebar:
    st.image("a.webp", width=200)
    
st.markdown(f"""
            <h1 style="color: #5EEAD4; font-family:'Courier New', Courier, monospace;">
           🅰️ About Me
            </h1>
            """, unsafe_allow_html=True)
st.markdown(f"""
 <p className='max-w-lg '>I am <strong className='text-teal-300'>Shaikh Abdul Moiz</strong>,a fresh front-end developer. I can
build cool websites using Next.js and also using React.js and
integrate typescript into these tools. It’s my passion to not
only develop websites for clients but also create a good user
experience for clients. It’s my mission to not compromise in
User Interface and User Experience. I have developed some
websites like E-commerce using Next.js which you can check
in my Portfolio.</p>
""",
unsafe_allow_html=True)

st.markdown(f"""
            <h3 style="color: #5EEAD4; font-family:'Courier New', Courier, monospace; padding-bottom:30px;">
            Education
            </h3>
            """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div style="border: 2px dashed #A8A8A8; padding:5px;"  >
    <p><strong style="color:#5EEAD4;  font-family:'Courier New', Courier, monospace;">School: </strong>CMS Govt Higher Secondary Campus School</p>
            <p><strong style="color:#5EEAD4;  font-family:'Courier New', Courier, monospace;">Passing Year: </strong>2021</p>
                </div>
""",unsafe_allow_html=True)
    
with col2:
      st.markdown(f"""
                  <div style="border: 2px dashed #A8A8A8; padding:5px;"  >
<p><strong style="color:#5EEAD4;  font-family:'Courier New', Courier, monospace;">College: </strong>SM Govt Sciene College</p>
            <p><strong style="color:#5EEAD4;  font-family:'Courier New', Courier, monospace;">Passing Year: </strong>2024</p>
                  </div>
""",unsafe_allow_html=True)