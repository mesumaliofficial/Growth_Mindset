import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(
    page_title="Python Projects",
    page_icon="🐍",
    layout="centered",
)

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

if selected == "Guess the Number (Com)":
    from guess_the_num import comp_guess
    comp_guess()

if selected == "Guess the Number (User)":
    from guess_num_user import user_guess
    user_guess()

if selected == "Rock, Paper, Scissors":
    from Rock_Paper_Scissor import play
    play()

if selected == "Hangman":
    from Hangman import hangman
    hangman()