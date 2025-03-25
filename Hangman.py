import streamlit as st
import random

def hangman():
    st.title("🎮 Hangman Game")
    st.subheader("Guess the word by entering letters. You have 6 chances. Good Luck! 🍀")
    st.markdown("---")

    if "word" not in st.session_state:
        st.session_state.word_list = ["apple", "banana", "cherry", "kiwi", "lemon", "mango", "orange", "strawberry"]
        st.session_state.word = random.choice(st.session_state.word_list)
        st.session_state.guessed_letters = set()
        st.session_state.attempts = 6
        st.session_state.game_over = False

    word_display = ""
    for letter in st.session_state.word:
        if letter in st.session_state.guessed_letters:
            word_display += f":green[{letter}] "
        else:
            word_display += ":red[_] "

    st.markdown(f"### Word: {word_display}")
    st.write(f"**Guessed Letters:** {', '.join(sorted(st.session_state.guessed_letters))}")
    st.write(f"**Remaining Attempts:** :orange[{st.session_state.attempts}]")

    guess = st.text_input("Enter a letter").lower()

    if st.button("Guess") and not st.session_state.game_over:
        if not guess.isalpha() or len(guess) != 1:
            st.warning(":warning: Please enter a single valid letter.")
        elif guess in st.session_state.guessed_letters:
            st.warning(":warning: You have already guessed that letter.")
        else:
            st.session_state.guessed_letters.add(guess)

            if guess in st.session_state.word:
                st.success(f"✅ Good guess! '{guess}' is in the word.")
                if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
                    st.balloons()
                    st.success(f"🎉 Congratulations! You guessed the word: **{st.session_state.word}**")
                    st.session_state.game_over = True
            else:
                st.session_state.attempts -= 1
                st.error(f"❌ Incorrect guess. Try again. **{st.session_state.attempts}** attempts left.")
                if st.session_state.attempts == 0:
                    st.error(f"💥 Game Over! The word was: **{st.session_state.word}**")
                    st.session_state.game_over = True

    if st.session_state.game_over and st.button("Play Again"):
        del st.session_state.word
        del st.session_state.guessed_letters
        del st.session_state.attempts
        del st.session_state.game_over
        st.experimental_rerun()
