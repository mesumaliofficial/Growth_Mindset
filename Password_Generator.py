import streamlit as st
import random

def password_generator():
    st.write("## 🔑 Password Generator")
    st.write("Generate strong and secure passwords instantly.")
    
    # Password Length
    password_length = st.slider("Password Length", 6, 25, 8)

    # Password Characters
    password_characters = st.multiselect("Select the Characters", ["Numbers", "Uppercase Letters", "Lowercase Letters", "Special Characters"])

    # Password Generation
    password = ""

    if "Numbers" in password_characters:
        password += "0123456789"

    if "Uppercase Letters" in password_characters:
        password += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if "Lowercase Letters" in password_characters:
        password += "abcdefghijklmnopqrstuvwxyz"

    if "Special Characters" in password_characters:
        password += "!@#$%^&*()_+[]{}"

    if st.button("Generate") and password != "":
        password = "".join(random.choices(password, k=password_length))
        st.success(f"✅ Generated Password: {password}")
