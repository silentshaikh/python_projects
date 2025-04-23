import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Portfolio - Skills",
    page_icon="🧑‍💻",
    layout="wide"
)

with st.sidebar:
    st.image("a.webp", width=200)


st.markdown(f"""
            <h1 style="color: #5EEAD4; font-family:'Courier New', Courier, monospace;">
           💡 Skills
            </h1>
            """, unsafe_allow_html=True)
st.markdown(f"""
            <p style="color: #A8A8A8; padding-bottom:20px; letter-spacing: 0ic; font-family:'Courier New', Courier, monospace;">
            Below, you can see the skills that I have learned!
            </p>
            """, unsafe_allow_html=True)

# Image url
imageUrl = "https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/r61eok59mh9jzk7f0klr"
skillList = [
    {
"name":'HTML',
        "img":"https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/f0huvqcjrih2czzr938g",
        "id":1,
        
    },
     {
"name":'CSS',
        "img":"https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/naag3civti2kzwdz5or3",
        "id":2,
    },
     {
"name":'JAVASCRIPT',
        "img":"https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/jbsjih1hkbbcvafg1ywv",
        "id":3,
    },
     {
"name":'TYPESCRIPT',
        "img":"https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/yz3j49ai5jx0aswyftpf",
        "id":4,
    },
     {
"name":'TAILWIND CSS',
        "img":"https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/h3fkvxu3vm5hixdxh5gu",
        "id":5,
    },
     {
"name":'NEXT.JS',
        "img":"https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/ae8clxy2xjkxzptslee9",
        "id":6,
    }
]

    # Create a centered container
with st.container():
    num_columns = 2  # Number of images in a row
cols = st.columns([1, 7, 1])  # Left, Center, Right (Center is wider)

with cols[1]:  # Center column
    img_cols = st.columns(num_columns)  # Two image columns with space in between
    for index, skill in enumerate(skillList):
        col_index = index % num_columns
        with img_cols[col_index ]:  # Place images in alternate slots
            st.markdown(
                f"""
                <div style="margin:10px 20px; padding:6px; text-align:center; background-color:#DEE1E3; display:flex; justify-content: center; align-items:center; gap:12px">
                    <img style="width:60px; height:25px; " src="{skill['img']}" alt="{skill['name']}" 
                    >
                    <h5 style="color:#A8A8A8; text-align:center; font-family:'Courier New', Courier, monospace; padding-top:5px;">{skill["name"]}</h5>
                </div>
                """,
                unsafe_allow_html=True,
            )