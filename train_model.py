import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load Excel
data = pd.read_excel("jade_data.xlsx")

# Chọn feature
X = data[[
    "Transparency (1–6)\nChủng",
    "Hue purity (0–4)\nTông màu",
    "Saturation (0–3)\nĐộ tươi",
    "Brightness (0–3)",
    "Uniformity (1–5)\nLoang màu",
    "Structural Risk (0–5)",
    "Diameter",
    "Thickness"
]]

# Target
y = data["Price\nlisted"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "jade_model.pkl")

print("Model trained successfully!")
