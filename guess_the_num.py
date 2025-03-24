import streamlit as st
import random

def comp_guess():
    st.title("🎲 Guess the Number")
    st.subheader("Can you guess the number I'm thinking of?")
    st.markdown("---")

    if "generate" not in st.session_state:
        st.session_state.generate = random.randint(1, 10)
        st.session_state.attempt = 0
        st.session_state.max_attempt = 3

    st.write(f"You have {st.session_state.max_attempt} attempts to guess the number.")
    guess = st.number_input("Enter your guess:", min_value=1, max_value=10)

    if st.button("Check"):
        st.session_state.attempt += 1

        if guess < st.session_state.generate:
            st.error(f"Too low! Attempts left: {st.session_state.max_attempt - st.session_state.attempt}")
        elif guess > st.session_state.generate:
            st.error(f"Too high! Attempts left: {st.session_state.max_attempt - st.session_state.attempt}")
        else:
            st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempt} attempts.")
            st.balloons()
            st.session_state.attempt = st.session_state.max_attempt  # End game

    if st.session_state.attempt >= st.session_state.max_attempt:
        st.error(f"You Lose! The number was {st.session_state.generate}.")
        if st.button("Play Again"):
            st.session_state.generate = random.randint(1, 10)
            st.session_state.attempt = 0

comp_guess()