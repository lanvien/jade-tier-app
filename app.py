import streamlit as st
import time
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
            "color_vibrancy": color_vibrancy,
            "crack": crack,
            "impurity": impurity,
            "size": size,
            "thickness": thickness
        }
        st.session_state.page = "loading"
        st.rerun()

# -----------------------------
# LOADING PAGE
# -----------------------------
def loading_page():
    st.title("⏳ Đang phân tích cốt ngọc và sắc diện...")

    messages = [
        "Ngọc dưỡng người 3 năm, người dưỡng ngọc một đời...",
        "Ngọc Phỉ Thuý càng đeo sẽ càng lên nước và bóng hơn...",
        "Đang đối chiếu dữ liệu thị trường...",
        "Đang kiểm tra chứng thư GIV, SJC, Liulab..."
    ]

    for msg in messages:
        st.write(msg)
        time.sleep(1)

    st.session_state.page = "result"
    st.rerun()

# -----------------------------
# RESULT PAGE
# -----------------------------
def result_page():
    st.title("✨ GIÁ TRỊ ƯỚC TÍNH CHIẾC VÒNG CỦA BẠN")

    data = st.session_state.data

    # Fake scoring
    score = (
        data["uniformity"] * 10 +
        data["color_vibrancy"] * 15 -
        data["crack"] * 10 -
        data["impurity"] * 5
    )

    min_price = int(5_000_000 + score * 10000)
    max_price = min_price + 2_500_000

    st.success(f"{min_price:,} VNĐ - {max_price:,} VNĐ")

    # Spider chart
    categories = ["Độ Trong", "Màu Sắc", "Độ Sạch", "Kích Thước", "Thẩm Mỹ"]
    values = [
        data["uniformity"],
        data["color_vibrancy"],
        4 - data["impurity"],
        data["thickness"],
        3
    ]

    values += values[:1]

    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_yticklabels([])

    st.pyplot(fig)

    col1, col2 = st.columns(2)

    if col1.button("Định giá vòng khác"):
        st.session_state.page = "home"
        st.rerun()

    if col2.button("Chia sẻ kết quả"):
        st.write("Tính năng chia sẻ sẽ cập nhật sau 💎")

# -----------------------------
# ROUTER
# -----------------------------
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "form":
    form_page()
elif st.session_state.page == "loading":
    loading_page()
elif st.session_state.page == "result":
    result_page()
