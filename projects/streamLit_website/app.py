import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Portfolio",
    page_icon="🧑‍💻",
    layout="wide"
)





# 🟢 Sidebar (Fixed on Left)
with st.sidebar:
    st.image("a.webp", width=200)  # Sidebar logo
    # if st.sidebar.button("🏡 Home Page"):
    #     st.switch_page("homepage")

    # if st.sidebar.button("🅰️ About Me"):
    #     st.switch_page("/pages/about")

    # if st.sidebar.button("🎓 Skills"):
    #     st.switch_page("/pages/skills")

    # if st.sidebar.button("📧 Contact Me"):
    #     st.switch_page("/pages/contact")

# 🟢 Main Content (2 Columns)
colOne, colTwo = st.columns([1, 2])  # First column is smaller, second is wider

with colOne:
    st.image("Snapchat.jpg", caption="", width=200)

with colTwo:
    st.markdown(f"""
    <span style="font-family:'Courier New', Courier, monospace; font-weight:bold; text-decoration:underline;">
    HI
    </span>
    """, unsafe_allow_html=True)

    st.markdown(f"""
            <h1 style="color: #5EEAD4; font-family:'Courier New', Courier, monospace;">
            Shaikh Abdul Moiz
            </h1>
            """, unsafe_allow_html=True)

    st.markdown(f"""
            <h3 style="color: #A8A8A8; letter-spacing: 0ic; font-family:'Courier New', Courier, monospace;">
            Front-End Developer
            </h3>
            """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    div.stDownloadButton > button {
        font-family:'Courier New', Courier, monospace;
        background-color: #5EEAD4; /* Custom background color */
        color: white; /* Text color */
        font-size: 18px; /* Font size */
        font-weight: bold; /* Bold text */
        border-radius: 5px; /* Rounded corners */
        padding: 10px; /* Padding */
        border: 2px solid white; /* Border color */
    }
    div.stDownloadButton > button:hover {
        border: 2px solid #A8A8A8;
        color:white;
    }
    </style>
""", unsafe_allow_html=True)

    st.download_button(
        label="📋 Download Resume ",
        data="Your resume file data here",  # Replace with actual PDF file data
        file_name="Resume - Abdul Moiz.pdf",
        mime="application/pdf"
    )

    st.markdown(f"""
            <h2 style="padding-top:30px; color: #BFFDEF; text-transform:uppercase; letter-spacing: 0ic; font-family:'Courier New', Courier, monospace;">
            Projects
            </h2>
            """, unsafe_allow_html=True)
    imageslist = [
    {"imageName": "Resume Builder", "imageUrl": "https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/qpqrpcke9ya16uhm9ut8", "imageId": 1, "link":"https://milestone-5-eta-hazel.vercel.app/"},
    {"imageName": "Fabric Haven", "imageUrl": "https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/v3fv18qpl1owt9y5qlbc", "imageId": 2, "link":"https://fabrichaven.vercel.app/"},
    {"imageName": "Portfolio", "imageUrl": "https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/dmez7kt7vy1a3incv4dm", "imageId": 3, "link":"https://portfolio-blush-gamma-80.vercel.app/"},
    {"imageName": "Coffee Haven", "imageUrl": "https://res.cloudinary.com/de3hsuhgv/image/upload/f_auto,q_auto/jdcflo1bovrth8bmtaag", "imageId": 4, "link":"https://coffee-haven.vercel.app/"},
]
    # Create a centered container
with st.container():
    num_columns = 2  # Number of images in a row
cols = st.columns([1, 7, 1])  # Left, Center, Right (Center is wider)

with cols[1]:  # Center column
    img_cols = st.columns(num_columns)  # Two image columns with space in between
    for index, img in enumerate(imageslist):
        col_index = index % num_columns
        with img_cols[col_index ]:  # Place images in alternate slots
            # st.image(img["imageUrl"], caption=img["imageName"], width=300)
            st.markdown(
                f"""
                <a href="{img['link']}" target="_blank">
                <div style="margin:0 20px;">
                    <img style="height:200px;" src="{img['imageUrl']}" alt="{img['imageName']}" 
                    >
                    <h5 style="color:#A8A8A8; text-align:center; font-family:'Courier New', Courier, monospace; padding-top:5px; text-decoration:none">{img["imageName"]}</h5>
                </div>
                </a>
                """,
                unsafe_allow_html=True,
            )
        