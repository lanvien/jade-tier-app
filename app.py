import streamlit as st
import time
import random
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# SESSION INIT
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------------
# HOME PAGE
# -----------------------------
def home_page():
    st.title("🌿 ĐỊNH GIÁ PHỈ THÚY")
    st.write("Chỉ dành cho phỉ thuý tự nhiên type A (không xử lý ép nhựa / nhuộm màu).")

    if st.button("Bắt đầu thẩm định ngay"):
        st.session_state.page = "form"
        st.rerun()

# -----------------------------
# FORM PAGE
# -----------------------------
def form_page():
    st.header("I. CỐT NGỌC")

    structure = st.radio(
        "Hạt tinh thể ngọc trông thế nào?",
        ["Đậu", "Nếp mịn", "Nếp băng"]
    )

    translucency = st.radio(
        "Chất ngọc trông thế nào?",
        ["Đục hoàn toàn", "Đục nhẹ", "Xuyên sáng vừa", "Xuyên sáng rõ"]
    )

    uniformity = st.slider("Độ đồng đều", 1, 4, 3)

    st.header("II. SẮC DIỆN")

    color = st.multiselect(
        "Màu quan sát được",
        ["Xanh lá", "Tím", "Vàng/Nâu", "Trắng", "Đỏ", "Đen", "Xám", "Xanh dương"]
    )

    color_vibrancy = st.slider("Độ tươi màu", 1, 4, 3)

    st.header("III. NỘI TẠI")

    crack = st.slider("Đường nứt", 0, 3, 0)
    impurity = st.slider("Tạp chất", 0, 3, 1)

    st.header("IV. KÍCH THƯỚC")

    size = st.number_input("Ni vòng (mm)", value=54)
    thickness = st.slider("Độ dày cảm nhận", 1, 3, 2)

    if st.button("Phân tích giá trị"):
        st.session_state.data = {
            "structure": structure,
            "translucency": translucency,
            "uniformity": uniformity,
            "color_vibrancy": color_vibrancy
