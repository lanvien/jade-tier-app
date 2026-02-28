import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Jade Tier Predictor", layout="centered")

st.title("💎 Jade Tier Predictor")

st.write("Enter your stats below to predict your tier.")

# -----------------------------
# Input Section
# -----------------------------
games_played = st.number_input("Games Played", min_value=0, value=100)
win_rate = st.slider("Win Rate (%)", 0, 100, 50)
avg_kda = st.number_input("Average KDA", min_value=0.0, value=2.5)

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Tier"):

    # Dummy model logic (replace later)
    score = (win_rate * 0.6) + (avg_kda * 10)

    if score > 120:
        tier = "Diamond"
    elif score > 90:
        tier = "Emerald"
    elif score > 70:
        tier = "Platinum"
    else:
        tier = "Gold"

    st.success(f"Predicted Tier: {tier}")
