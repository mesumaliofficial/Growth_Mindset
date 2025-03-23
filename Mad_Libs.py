import streamlit as st

def generate_madlibs():
    st.title("🌈 Madlibs Kahani Generator")
    st.subheader("Apni kahani banayein apni pasand ke alfaaz se!")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Input Form")
        animal = st.text_input("🦾 Ek janwar ka naam likhein:")
        transport = st.text_input("🚌 Kisi safar ke zariye ka naam likhein (jaise bus, train):")
        food = st.text_input("🍔 Khanay ka naam likhein:")
        
    with col2:
        st.header("...")
        place = st.text_input("📍 Kisi jagah ka naam likhein:")
        dost = st.text_input("👫 Kisi dost ka naam likhein:")

    if st.button("Generate Story"):
        if all([animal, place, transport, dost, food]):
            story = f"""
        ## 🌟 Aapki Kahani 🌟

        Ek din, ek chhota sa **{animal}** apne **{place}** ke paas baitha tha. 
        Woh hamesha se kisi naye jagah ka safar karna chahta tha. 
        Aik din usne faisla kiya ke woh ek lambi **{transport}** ka safar karega.

        Usne apni chhoti si potli uthai aur sheher ke station ki taraf nikal para. 
        Rastay me usay ek mehboob dost, **{dost}** mila jo ek purani kitaab ko sambhal raha tha.

        "**{dost}**, agar tum bhi safar par ja rahe ho, to kya mujhe apne sath le ja sakte ho?" **{animal}** ne poocha. 
        **{dost}** ne khushi se haan kar di.

        Dono **{transport}** me baithe aur safar shuru ho gaya. 
        Sheher ke khubsurat manzar unke samne tez raftari se guzar rahe the. 
        Raaste me unhon ne **{food}** ka maza liya aur naye logon se mile.

        Yeh safar dono ke liye ek yaadgar tajurba bana! 🚀
        """
            st.success("Kahani Tayar Hai!")
            st.markdown(story)
        else:
            st.warning("Please fill all the fields to generate the story.")
