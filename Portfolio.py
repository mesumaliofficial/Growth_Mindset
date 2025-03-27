import streamlit as st

def portfolio():

    st.markdown("""
            <style>
            .profile-pic {
                border-radius: 150px;
                border: 2px solid gray;
                width: 200px;
                height: 200px;
                object-fit: center;
            }
            h1.name {
                font-size: 28px;
                background: linear-gradient(90deg, #ffffff, #808080);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: bold;
                color: blue;
            }
            .st-emotion-cache-mtjnbi {
                padding: 2.5rem 1rem 10rem;
            }

            </style>
        """, unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <img src="https://raw.githubusercontent.com/mesumaliofficial/Growth_Mindset/refs/heads/main/myPic.jpg" class="profile-pic">
            
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown("""
        <h1 class="name">Syed Mesum Ali Shah</h1>
        <p>Next js Full Stack Developer | HTML, Css, Typescript, JavaScript, Python Tailwind, Bootstrap...</p>
        """, 
        unsafe_allow_html=True)
        st.button("📧 Contact Me")
        st.markdown("""
        <p>✉️ syedmesumjaffary@gmail.com</p>
        """, unsafe_allow_html=True)

        st.write("")
        st.write("")

    col1, col2, col3, col4 = st.columns(4,)

    with col1:
        st.write("Youtube")
    
    with col2: 
        st.write("Linkedin")

    with col3: 
        st.write("Github")

    with col4: 
        st.write("Twitter")

    st.write("")
    st.subheader("Qualifications")
    st.markdown("""
    ✔️  **Intermediate** completed from *Jamia Milia College*  
    ✔️  **Matriculation** completed from *Sunrise Children Academy School*  
    """)

    st.write("")
    st.subheader("Experience")
    st.markdown('✔️ <b>Internship</b> — 3 months at Plug IT Solution', unsafe_allow_html=True)

    st.subheader("Certefications")
    st.markdown("""
    ✔️ <b>Web Designing</b> — 8 Months<br>
    ✔️ <b>Fast Project Completion</b> — from Plug IT Solution
    """, unsafe_allow_html=True)
