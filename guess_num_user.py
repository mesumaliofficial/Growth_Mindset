import streamlit as st
import random

def user_guess():
    st.title("🤖 Computer Guesses the Number")
    st.subheader("Think of a number and let the computer guess!")
    st.markdown("---")

    if "low" not in st.session_state:
        st.session_state.low = 1
        st.session_state.high = 10
        st.session_state.game_over = False
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
        st.session_state.attempt = 1

    if not st.session_state.game_over:
        st.write(f"🤖 **Computer's Guess:** {st.session_state.guess}")
    
        feedback = st.radio(
            "Tell us more about the guess:",
            ["Too low", "Too high", "Correct"],
            key=f"feedback_{st.session_state.guess}")
        
        if st.button("Submit Feedback"):
            if feedback == "Too low":
                st.session_state.low = st.session_state.guess + 1
            elif feedback == "Too high":
                st.session_state.high = st.session_state.guess - 1
            else:
                st.success(f"🎉 Computer guessed the number in {st.session_state.attempt} attempts.")
                st.balloons()
                st.session_state.game_over = True

            if st.session_state.low <= st.session_state.high and not st.session_state.game_over:
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
                st.session_state.attempt += 1

    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.low = 1
            st.session_state.high = 10
            st.session_state.game_over = False
            st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            st.session_state.attempt = 1

user_guess()