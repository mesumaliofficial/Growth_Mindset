import streamlit as st
import random

def play():
    st.title("Rock, Paper, Scissors 🎮")
    st.markdown("### Test your luck against the computer!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Your Choice")
        user_choice = st.selectbox(
            "Choose",
            ["Rock", "Paper", "Scissors"]
        )

    if st.button("Play", key="play_button"):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        st.markdown(f"### 💻 Computer chose: **{computer_choice}**")

        if user_choice == computer_choice:
            st.success("It's a tie!", icon="🔄")
        elif user_choice == "Rock" and computer_choice == "Scissors":
            st.success("You win!", icon="🏆")
        elif user_choice == "Paper" and computer_choice == "Rock":
            st.success("You win!", icon="🏆")
        elif user_choice == "Scissors" and computer_choice == "Paper":
            st.success("You win!", icon="🏆")
        else:
            st.error("Computer wins!", icon="💻")
