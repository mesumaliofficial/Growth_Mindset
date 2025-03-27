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
            <img src="https://scontent.fkhi2-3.fna.fbcdn.net/v/t39.30808-6/457450255_1994882280928472_2597714411168026824_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=107&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeF07rF8Rp1WdlAhN_-72zm2Q9VtOXdaqXtD1W05d1qpe_VeLU1NLGxU3wRV0ayhm3BnRn5olbPsSXC5LDGtps1a&_nc_ohc=w-iPFZjq4roQ7kNvgG31rNG&_nc_oc=AdlfI-i-AsDdtFbtX4mtMdhFrcQ9pDlSl5dTQ2KdM32Suz1rmj_jbbUt2B-NuMJ8JcY&_nc_zt=23&_nc_ht=scontent.fkhi2-3.fna&_nc_gid=sEnvpZYQKKf34R577l5tXQ&oh=00_AYEVP-cC9jO5cMmn66NvhxVzf77QEM3tLL_OzFEOOOcJcg&oe=67EAFC54" class="profile-pic">
            
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
