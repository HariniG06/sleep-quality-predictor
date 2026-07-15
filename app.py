import streamlit as st
import numpy as np
import joblib

# Load Model
model = joblib.load("sleep_quality_model.pkl")

# Page Config
st.set_page_config(
    page_title="Sleep Quality Predictor",
    page_icon="😴",
    layout="wide"
)

# Black & Gold Theme
st.markdown("""
<style>

.stApp{
    background-color:#121212;
}

.main-title{
    text-align:center;
    color:#FFD700;
    font-size:45px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:white;
    font-size:18px;
    margin-bottom:20px;
}

.stButton button{
    background:#D4AF37;
    color:black;
    font-size:20px;
    font-weight:bold;
    border-radius:12px;
    height:60px;
    width:100%;
    border:none;
}

.stButton button:hover{
    background:#FFD700;
    color:black;
}

label{
    color:white !important;
}

[data-testid="stMarkdownContainer"]{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<p class="main-title">😴 Sleep Quality Predictor</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Predict Sleep Quality using Lifestyle and Health Data</p>',
    unsafe_allow_html=True
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=25
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "Engineer",
            "Doctor",
            "Teacher",
            "Nurse",
            "Lawyer",
            "Scientist",
            "Manager",
            "Accountant",
            "Salesperson",
            "Student"
        ]
    )

    st.subheader("😴 Sleep Duration")

    h1, h2 = st.columns(2)

    with h1:
        sleep_hours = st.number_input(
            "Hours",
            min_value=0,
            max_value=12,
            value=7
        )

    with h2:
        sleep_minutes = st.selectbox(
            "Minutes",
            [0, 15, 30, 45]
        )

    sleep_duration = sleep_hours + (sleep_minutes / 60)

    physical_activity = st.slider(
        "Physical Activity Level",
        0,
        100,
        50
    )

with col2:

    stress_level = st.slider(
        "Stress Level",
        0,
        10,
        5
    )

    bmi = st.selectbox(
        "BMI Category",
        [
            "Normal",
            "Overweight",
            "Obese",
            "Underweight"
        ]
    )

    blood_pressure = st.selectbox(
        "Blood Pressure",
        [
            "Low",
            "Normal",
            "High"
        ]
    )

    heart_rate = st.number_input(
        "Heart Rate",
        min_value=40,
        max_value=150,
        value=75
    )

    daily_steps = st.number_input(
        "Daily Steps",
        min_value=0,
        max_value=30000,
        value=5000
    )

    sleep_disorder = st.selectbox(
        "Sleep Disorder",
        [
            "None",
            "Insomnia",
            "Sleep Apnea"
        ]
    )

# Encoding
gender_map = {
    "Female": 0,
    "Male": 1
}

occupation_map = {
    "Student":0,
    "Engineer":1,
    "Doctor":2,
    "Teacher":3,
    "Nurse":4,
    "Manager":5,
    "Scientist":6,
    "Lawyer":7,
    "Salesperson":8,
    "Accountant":9
}

bmi_map = {
    "Underweight":0,
    "Normal":1,
    "Overweight":2,
    "Obese":3
}

bp_map = {
    "Low":0,
    "Normal":1,
    "High":2
}

sleep_disorder_map = {
    "None":0,
    "Insomnia":1,
    "Sleep Apnea":2
}

if st.button("🔍 Predict Sleep Quality"):

    data = np.array([[
        gender_map[gender],
        age,
        occupation_map[occupation],
        sleep_duration,
        physical_activity,
        stress_level,
        bmi_map[bmi],
        bp_map[blood_pressure],
        heart_rate,
        daily_steps,
        sleep_disorder_map[sleep_disorder]
    ]])

    prediction = model.predict(data)[0]
    score = round(float(prediction), 1)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#D4AF37,#FFD700);
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:black;">
        <h1>😴 Sleep Quality Score</h1>
        <h1>{score}/10</h1>
    </div>
    """, unsafe_allow_html=True)

    st.progress(min(int(score * 10), 100))

    if score >= 8:
        st.balloons()
        st.success("🌙 Excellent Sleep Quality")

    elif score >= 6:
        st.warning("😐 Average Sleep Quality")

    else:
        st.error("⚠️ Poor Sleep Quality")

    st.markdown("### 💡 Recommendations")

    st.success("✅ Sleep 7–8 hours daily")
    st.success("✅ Reduce stress levels")
    st.success("✅ Exercise regularly")
    st.success("✅ Reduce mobile usage before sleep")
    st.success("✅ Maintain a consistent sleep schedule")