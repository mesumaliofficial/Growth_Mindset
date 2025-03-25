import streamlit as st      
import time

def countdownTimer():
    st.title("⏱️ Countdown Timer")
    st.write("Set the countdown time in Hours, Minutes, and Seconds")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        hours = st.number_input("🕰 Hours", 0, 23, 0)
    with col2:
        minutes = st.number_input("⏳ Minutes", 0, 59, 0)
    with col3:
        seconds = st.number_input("⏱️ Seconds", 0, 59, 0)

    total_seconds = hours * 3600 + minutes * 60 + seconds

    def countdown(time_sec):
        time_placeholder = st.empty()
        st.markdown("---")

        progress_bar = st.progress(0)
        initial_time = time_sec

        while time_sec > 0:
            hrs, rem = divmod(time_sec, 3600)
            mins, secs = divmod(rem, 60)

            time_format = f"<h1 style='text-align: center; color: #FF4B4B;'>{hrs:02d}:{mins:02d}:{secs:02d}</h1>"

            time_placeholder.markdown(time_format, unsafe_allow_html=True)
            progress = (initial_time - time_sec) / initial_time
            progress_bar.progress(progress)

            time.sleep(1)
            time_sec -= 1
        progress_bar.progress(1.0)
        st.success("🎉 Countdown Finished!")
        st.balloons()
         
        if st.button("Reset Timer"):
            st.experimental_rerun()

    if st.button("Start Timer"):
        if total_seconds > 0:
            countdown(total_seconds)
        else:
            st.warning("Please set a time for the countdown")

    