import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="📚",
    layout="wide"
)

st.markdown(f"""
            <div style="display:flex; justify-content:center; padding:10px;
            box-shadow: rgba(0, 0, 0, 0.04) 0px 3px 5px; border-radius:10px; margin-bottom:50px;
            ">
            <h1 style="color: #5EEAD4; font-family:'Courier New', Courier, monospace;">
            BMI Calculator

            </h1>
            </div>
            """, unsafe_allow_html=True)



# calculator form

# weight input

weightInput = st.number_input("Enter your Weight (KG) : ",min_value=1)
heightInput = st.number_input("Enter your Height (CM) : ",min_value=1)
bmiBtn =  st.button("Calculate")
if bmiBtn:

    if not weightInput or not heightInput:
        st.error("❌ Please Fill all the fields")
    else:
        heightInMeter = heightInput/100
        bmiValue = round((weightInput/(heightInMeter**2)),2)
        st.markdown(f"""
            <div style="display:flex; justify-content:center; padding:10px;
            box-shadow: rgba(0, 0, 0, 0.04) 0px 3px 5px; border-radius:10px; margin-bottom:50px;
            ">
            <h3 style=" font-family:'Courier New', Courier, monospace;">
            <strong style="color: #5EEAD4;">Your BMI is : </strong> {bmiValue} kg/m²

            </h3>
            </div>
            """, unsafe_allow_html=True)
        st.balloons()
        

