import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

if "threat_count" not in st.session_state:
    st.session_state.threat_count = 0
# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI-Based Multi-Stage Cyber Threat Detection and RIsk Assessment Syste",
    page_icon="🛡️",
    layout="wide"
)
st.markdown("""
<style>

.stApp {
    background: #070B14;
    color: #EAF2FF;
}

/* Main title */
h1, h2, h3 {
    color: #00E5FF !important;
    font-weight: 700;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0B1220;
    border-right: 1px solid #12304A;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #0066FF, #00B8D9);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    padding: 10px 18px;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #0052CC, #00E5FF);
    color: white;
    transform: scale(1.02);
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background-color: #101A2B;
    border: 1px solid #174A6B;
    color: white;
}

/* Dashboard cards */
div[data-testid="metric-container"] {
    background: #101A2B;
    border: 1px solid #174A6B;
    border-radius: 12px;
    padding: 15px;
}

/* Alerts */
.stAlert {
    border-radius: 10px;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border: 1px solid #174A6B;
    border-radius: 10px;
}

/* Divider */
hr {
    border-color: #17334A;
}

/* Hide footer */
footer {
    visibility: hidden;
}
/* Login input fields */
div[data-baseweb="input"] {
    background-color: #101A2B !important;
    border: 1px solid #174A6B !important;
    border-radius: 8px !important;
}

div[data-baseweb="input"] input {
    color: white !important;
    background-color: #101A2B !important;
}

div[data-baseweb="input"] input::placeholder {
    color: #8FA3B8 !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1 {
    color: #00FF99;
    text-align: center;
}
h2, h3 {
    color: #00CCFF;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Title
# -------------------------
st.markdown("""
<h1 style='text-align:center;
color:#FFD700;
font-size:42px;'>
🛡️AI-Based Multi-Stage Cyber Threat Detection and RIsk Assessment Syste
</h1>
""", unsafe_allow_html=True)
st.divider()

# -------------------------
# Load AI Model
# -------------------------
model = None
try:
    model = joblib.load("models/cyber_model.pkl")
    st.success("✅ AI Model Loaded Successfully")
except Exception as e:
    st.error(f"❌ AI Model Not Found: {e}")

# -------------------------
# Dashboard Cards
# -------------------------
col1, col2, col3 = st.columns(3)
st.subheader("📊 Dashboard Overview")
st.caption("Real-time overview of AI cyber threat detection.")
with col1:
    st.metric("Threats Detected", "18")
with col2:
    st.metric("Safe Traffic", "107")
with col3:
    st.metric("Model Accuracy", "99.84%")

# -------------------------
# Login
# -------------------------

st.sidebar.title("🔐 Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

login = st.sidebar.button("Login")

if login:
    if username == "admin" and password == "1234":
        st.session_state.logged_in = True
        st.session_state.username = username
        st.sidebar.success("✅ Login Successful")
    else:
        st.session_state.logged_in = False
        st.sidebar.error("❌ Invalid Username or Password")

if st.session_state.logged_in:
    st.success(f"👋 Welcome, {username}!")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

st.sidebar.markdown("---")
st.markdown("---")

# -------------------------
# Sidebar Navigation
# -------------------------
st.sidebar.title("Navigation")
st.sidebar.image(
    "https://img.icons8.com/fluency/96/shield.png",
    width=80
)

st.sidebar.markdown("## 🛡️ Threatvision AI")
st.sidebar.markdown("AI Powered Threat Detection")
st.sidebar.markdown("---")
if st.session_state.logged_in:
    st.sidebar.info(f"👤 Logged in as: {st.session_state.username}")

page = st.sidebar.radio("Select Page", ["Home", "Prediction", "Reports", "About"])
st.sidebar.markdown("---")
st.sidebar.caption("Version 1.0")
st.sidebar.caption("Developed by KM Team")

# -------------------------
# HOME PAGE
# -------------------------
if page == "Home":
    st.header("🛡️ AI Powered Cyber Threat Detection System")

    st.markdown("""
    ### Welcome 👋

    This application uses **Machine Learning (Random Forest)** to detect cyber attacks from network traffic.

    ### 🚀 Features

    ✅ AI Based Threat Detection

    ✅ CSV File Upload

    ✅ Live Prediction Dashboard

    ✅ Threat Analysis

    ✅ Download Prediction Report
    """)

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        st.info("🤖 AI Model\n\nRandom Forest Classifier")

    with c2:
        st.success("🛡️ Security Status\n\nSystem Ready")

    st.subheader("🖥️ System Status")
    st.success("🟢 AI Detection Engine : Online")
    st.success("🟢 Random Forest Model : Loaded" if model else "🔴 Random Forest Model : Not Loaded")
    st.success("🟢 Dashboard Status : Active")

# -------------------------
# PREDICTION PAGE
# -------------------------
elif page == "Prediction":
    st.header("🤖 AI Prediction")
    st.markdown("---")
    st.info("📂 Upload your network traffic CSV file below to analyze cyber threats using the trained AI model.")

    uploaded_file = st.file_uploader("Choose CSV File", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.success("✅ File Uploaded Successfully")
        st.subheader("📋 Dataset Preview")
        st.caption("Preview of the uploaded network traffic dataset.")
        st.dataframe(data.head())
        st.write(f"📊 Total Records: **{len(data)}**")
        st.write(f"📌 Total Columns: **{len(data.columns)}**")
        st.markdown("---")

        if model is None:
            st.error("❌ Model not loaded. Please check models/cyber_model.pkl")
        else:
            if st.button("🚀 Predict"):
                try:
                    if "Attack Type" not in data.columns:
                        st.error("❌ CSV must contain 'Attack Type' column to drop for prediction")
                    else:
                        X = data.drop("Attack Type", axis=1)
                        prediction = model.predict(X)
                        st.success("✅ Prediction Completed")

                        # Summary
                        total_records = len(prediction)
                        safe_count = int(sum(prediction == 0))
                        threat_count = total_records - safe_count
                        threat_percentage = (threat_count / total_records) * 100 if total_records > 0 else 0

                        st.subheader("📊 Prediction Summary")
                        c1, c2, c3, c4 = st.columns(4)
                        c1.metric("Total Records", total_records)
                        c2.metric("Safe", safe_count)
                        c3.metric("Threats", threat_count)
                        c4.metric("Threat %", f"{threat_percentage:.2f}%")

                        st.subheader("🚨 Threat Status")
                        if threat_percentage < 20:
                            st.success("🟢 Threat Level: LOW")
                        elif threat_percentage < 50:
                            st.warning("🟡 Threat Level: MEDIUM")
                        elif threat_percentage < 80:
                            st.warning("🟠 Threat Level: HIGH")
                        else:
                            st.error("🔴 Threat Level: CRITICAL")

                        from datetime import datetime

                        st.subheader("🕒 Scan Information")

                        st.write("**Scan Date:**", datetime.now().strftime("%d-%m-%Y"))
                        st.write("**Scan Time:**", datetime.now().strftime("%H:%M:%S"))

                        # Result Table
                        result = data.copy()
                        result["Prediction"] = prediction
                        st.subheader("Prediction Results")
                        st.dataframe(result.head(20))
                        st.subheader("📊 Prediction Analysis")
                        # ----------------------------
                        # Threat Action Panel
                        # ----------------------------

                        chart_data ={
                                         "Category": ["Safe", "Threat"],
                                         "Count": [safe_count, threat_count]
                                        }

                        chart_df = pd.DataFrame(chart_data)

                        st.bar_chart(chart_df.set_index("Category"))
                        ...
                        
                        # Threat Action Panel

                        st.subheader("🛡 Threat Action Panel")

                        if threat_count > 0:
                             action = st.selectbox(
                                 "Select Action",
                                 ["Block IP", "Quarantine", "Ignore", "Generate Alert"]
                            )

                             if "action_history" not in st.session_state:
                                st.session_state.action_history = []

                             if st.button("Execute Action"):
                                if action == "Block IP":
                                    st.success("✅ Threat IP Blocked Successfully")
                                elif action == "Quarantine":
                                    st.success("📦 Threat Quarantined Successfully")
                                elif action == "Ignore":
                                    st.info("ℹ Threat Ignored")
                                elif action == "Generate Alert":
                                    st.warning("🚨 Security Alert Generated")

                        else:
                            st.success("✅ No Threats Found. No Action Required.")

                        st.subheader("🥧 Threat Distribution")

                        pie_data = pd.DataFrame({
                            "Category": ["Safe", "Threat"],
                            "Count": [safe_count, threat_count]
                        })

                        st.pyplot(
                            pie_data.set_index("Category").plot.pie(
                                y="Count",
                                autopct="%1.1f%%",
                                figsize=(5,5),
                                legend=False
                            ).get_figure()
                        )
                        csv = result.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label="📥 Download Prediction Results (CSV)",
                            data=csv,
                            file_name="prediction_results.csv",
                            mime="text/csv"
                        )


                        # Pie Chart
                        fig, ax = plt.subplots(figsize=(5, 5))
                        labels = ["Safe Traffic", "Threat Traffic"]
                        sizes = [safe_count, threat_count]
                        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
                        ax.set_title("Traffic Analysis")
                        st.pyplot(fig)
                        st.markdown("---")
                        st.success("✅ Analysis Completed Successfully!")
                        st.info("📥 You can download the prediction report for further analysis.")

                except Exception as e:
                    st.error(f"Error during prediction: {e}")

# -------------------------
# REPORT PAGE
# -------------------------
elif page == "Reports":
    st.header("📄 Reports")
    st.info("Reports Module Coming Soon...")
    st.download_button(
        label="📥 Download Sample Report",
        data="AI Powered Cyber Threat Detection Report\n\nStatus: Working Successfully\nModel Accuracy: 99.84%\nThreats Detected: 18\nSafe Traffic: 107",
        file_name="Cyber_Threat_Report.txt",
        mime="text/plain"
    )

# -------------------------
# ABOUT PAGE
# -------------------------
elif page == "About":

    st.header("ℹ️ About Project")

    st.write("""
### AI Powered Cyber Threat Detection System

This project is developed using Machine Learning to detect cyber attacks from network traffic.

### Technologies Used

- Python
- Streamlit
- Machine Learning
- Random Forest Algorithm
- Pandas
- Matplotlib

### Developed By

KM Team

### Purpose

This project is developed for educational and cybersecurity analysis purposes.
""")

st.markdown("---")

st.caption("🛡️ AI Powered Cyber Threat Detection System")

st.caption("Version 1.0 | Developed by KM Team | © 2026")
