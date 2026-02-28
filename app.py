import streamlit as st

# ===== Session state setup =====
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "score" not in st.session_state:
    st.session_state.score = 0

# ===== WELCOME PAGE =====
if st.session_state.page == "welcome":
    st.title("💎 Jade Tier Recommendation")
    st.write("Answer a few questions to find your perfect jade tier!")

    if st.button("Start"):
        st.session_state.page = "question"


# ===== QUESTION PAGE =====
elif st.session_state.page == "question":
    st.title("Question 1")

    answer = st.radio(
        "What matters most to you?",
        ["Luck & fortune", "Health & protection", "Luxury & status"]
    )

    if st.button("Next"):
        if answer == "Luck & fortune":
            st.session_state.score = 1
        elif answer == "Health & protection":
            st.session_state.score = 2
        else:
            st.session_state.score = 3

        st.session_state.page = "transition"


# ===== TRANSITION PAGE =====
elif st.session_state.page == "transition":
    st.title("Analyzing your energy... ✨")
    st.write("Calculating your jade compatibility...")

    if st.button("See Result"):
        st.session_state.page = "result"


# ===== RESULT PAGE =====
elif st.session_state.page == "result":
    st.title("Your Jade Tier 💎")

    if st.session_state.score == 1:
        st.success("Tier 1: Prosperity Jade")
    elif st.session_state.score == 2:
        st.success("Tier 2: Protection Jade")
    else:
        st.success("Tier 3: Imperial Jade")

    st.write("Thank you for taking the quiz!")
