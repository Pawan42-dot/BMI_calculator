import streamlit as st

st.title(" Smart BMI Calculator")


unit = st.radio("Select Height Unit:", ["Meters", "Feet & Inches"])

weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")

if unit == "Meters":
    height = st.number_input("Enter your height (meters):", min_value=0.0, format="%.2f")
else:
    feet = st.number_input("Feet:", min_value=0, format="%d")
    inches = st.number_input("Inches:", min_value=0, format="%d")
    height = (feet * 0.3048) + (inches * 0.0254)


calculate = st.button("Calculate BMI ")


if calculate:
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)

        st.info(f" **Your BMI is:** `{bmi:.2f}`")

        
        if bmi < 18.5:
            st.warning(" Underweight — You should gain some healthy weight.")
            st.write(" Add protein-rich foods & consult a nutritionist.")
        elif 18.5 <= bmi < 24.9:
            st.success(" Normal — Great job! Maintain your lifestyle.")
            st.write(" Keep exercising & eating balanced meals.")
        elif 25 <= bmi < 29.9:
            st.warning(" Overweight — Try to stay active & improve diet.")
            st.write(" Add fiber, reduce sugary food, increase workouts.")
        else:
            st.error("Obese — Plan for a healthy lifestyle change.")
            st.write(" Consult a doctor & follow a structured fitness plan.")

        
        st.progress(min(bmi / 40, 1.0))

    else:
        st.error("Please enter valid height and weight!")


st.subheader(" Importance of BMI")
st.write("""
BMI helps understand if your weight is healthy according to your height.
However, it does not consider:  
. Muscles  
. Body shape  
. Medical conditions  
. Lifestyle  


""")
