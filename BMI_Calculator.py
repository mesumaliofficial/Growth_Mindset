import streamlit as st

def bmi_calculator():
    st.title("🏋️ BMI Calculator")
    st.write("### Calculate your Body Mass Index (BMI) and check your health status.")
    st.markdown("---")
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("Enter your details:")
        weight = st.number_input("Enter your weight (in kg)", min_value=0.0, max_value=635.0, step=0.1)
    
    with col2:
        st.subheader("📝")
        height_inch = st.number_input("Enter your height (in inches)", min_value=0.0, max_value=107.0, step=0.1)
        
    
    if st.button("Calculate BMI") and height_inch > 0:
        # Convert height from inches to cm
        height_cm = height_inch * 2.54
        
        bmi = weight / ((height_cm / 100) ** 2)
        st.write(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            st.success("🍎 You are **Underweight**. Consider a nutritious diet.")
        elif 18.5 <= bmi < 25:
            st.success("🏆 You have a **Normal weight**. Keep it up!")
        elif 25 <= bmi < 30:
            st.warning("🍔 You are **Overweight**. Consider regular exercise.")
        else:
            st.error("🔥 You are **Obese**. Consult a healthcare provider.")
    

