import streamlit as st
from streamlit_option_menu import option_menu

st.markdown("""
    <style>
        .st-emotion-cache-a6qe2i {
            padding: 0px 5px !important;
        }
        .st-emotion-cache-kgpedg {
            padding: calc(1.375rem) 1.5rem 1rem;
            }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Python Projects",
        options=[
            "Mad Libs",
            "Guess the Number (Com)",
            "Guess the Number (User)",
            "Rock, Paper, Scissors",
            "Hangman",
            "Countdown Timer",
            "Password Generator",
            "BMI Calculator",
            "Python Website"
        ],
        icons=["book", "123", "123", "scissors", "puzzle",
               "hourglass", "key", "calculator", "globe"],
        menu_icon="code-square",
    )
    
if selected == "Mad Libs":
    from Mad_Libs import generate_madlibs
    generate_madlibs()