import streamlit as st
import pickle
import numpy as np

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Cherry Sales Predictor",
    page_icon="🍒",
    layout="centered"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
@st.cache_resource
def load_model():
    with open("linear_reg.sav", "rb") as file:
        return pickle.load(file)

model = load_model()

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Pacifico&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.75) 0%, transparent 20%),
        radial-gradient(circle at 90% 80%, rgba(255,255,255,0.60) 0%, transparent 22%),
        linear-gradient(135deg, #fff7fa 0%, #ffeaf0 50%, #ffdce6 100%);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 760px;
}

/* Hide default Streamlit elements */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Decorative cherries */
.cherry-left {
    position: fixed;
    top: 90px;
    left: 4%;
    font-size: 55px;
    transform: rotate(-12deg);
    opacity: 0.85;
    z-index: 0;
}

.cherry-right {
    position: fixed;
    bottom: 60px;
    right: 5%;
    font-size: 60px;
    transform: rotate(12deg);
    opacity: 0.85;
    z-index: 0;
}

/* Main card */
.hero-card {
    background: rgba(255, 255, 255, 0.80);
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 30px;
    padding: 30px 25px;
    margin-bottom: 30px;
    text-align: center;
    box-shadow: 0 15px 40px rgba(180, 70, 110, 0.12);
}

.small-cherry {
    font-size: 38px;
    margin-bottom: 4px;
}

.app-title {
    font-family: 'Pacifico', cursive;
    color: #c7345d;
    font-size: 46px;
    line-height: 1.2;
    margin-bottom: 8px;
}

.app-subtitle {
    color: #8d5264;
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 15px;
}

.mini-text {
    display: inline-block;
    background: #ffe0e9;
    color: #b33459;
    padding: 7px 15px;
    border-radius: 50px;
    font-size: 12px;
    font-weight: 600;
}

/* Section heading */
.section-title {
    font-size: 19px;
    font-weight: 700;
    color: #973550;
    margin-bottom: 14px;
}

/* Input labels */
label {
    color: #8c3651 !important;
    font-weight: 600 !important;
}

/* Input box */
div[data-baseweb="input"] {
    background-color: rgba(255,255,255,0.92) !important;
    border: 1.5px solid #f2b2c5 !important;
    border-radius: 15px !important;
    box-shadow: 0 5px 15px rgba(180, 60, 100, 0.05);
}

div[data-baseweb="input"]:focus-within {
    border: 1.5px solid #d94b70 !important;
    box-shadow: 0 0 0 3px rgba(217, 75, 112, 0.10);
}

/* Predict button */
.stButton > button {
    width: 100%;
    height: 55px;
    border: none;
    border-radius: 16px;
    background: linear-gradient(135deg, #df5579, #bf3158);
    color: white;
    font-size: 17px;
    font-weight: 700;
    box-shadow: 0 8px 20px rgba(190, 49, 86, 0.22);
    transition: 0.25s ease;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #cf3d65, #aa254a);
    color: white;
    transform: translateY(-2px);
}

.stButton > button:active {
    transform: scale(0.98);
}

/* Result card */
.result-card {
    margin-top: 25px;
    background: rgba(255,255,255,0.88);
    border: 2px solid #f2b4c6;
    border-radius: 24px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 12px 30px rgba(180, 60, 100, 0.12);
}

.result-label {
    color: #965469;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.result-number {
    color: #c72e58;
    font-size: 48px;
    font-weight: 800;
    margin: 4px 0;
}

.result-note {
    color: #a45f74;
    font-size: 13px;
}

/* Footer */
.footer {
    text-align: center;
    color: #b77b8d;
    font-size: 12px;
    margin-top: 35px;
    margin-bottom: 10px;
}

</style>
""",
    unsafe_allow_html=True
)

# --------------------------------------------------
# DECORATIVE CHERRIES
# --------------------------------------------------
st.markdown(
    """
<div class="cherry-left">🍒</div>
<div class="cherry-right">🍒</div>
""",
    unsafe_allow_html=True
)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown(
    """
<div class="hero-card">
<div class="small-cherry">🍒</div>
<div class="app-title">Cherry Sales</div>
<div class="app-subtitle">
Turn your advertising budget into a sweet little sales forecast.
</div>
<span class="mini-text">✨ Powered by Machine Learning</span>
</div>
""",
    unsafe_allow_html=True
)

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------
st.markdown(
    '<div class="section-title">🌸 Enter your advertising budget</div>',
    unsafe_allow_html=True
)

TV = st.number_input(
    "📺 TV Advertising Budget",
    min_value=0.0,
    value=0.0,
    step=1.0
)

Radio = st.number_input(
    "🎧 Radio Advertising Budget",
    min_value=0.0,
    value=0.0,
    step=1.0
)

Newspaper = st.number_input(
    "📰 Newspaper Advertising Budget",
    min_value=0.0,
    value=0.0,
    step=1.0
)

st.write("")

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------
if st.button("🍒 Predict My Sales"):

    input_data = np.array([[TV, Radio, Newspaper]])

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
<div class="result-card">
<div style="font-size:34px;">🍒</div>
<div class="result-label">YOUR PREDICTED SALES</div>
<div class="result-number">{prediction:.2f}</div>
<div class="result-note">
Sweet! Here's what your advertising mix could deliver ✨
</div>
</div>
""",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
<div class="footer">
Made with ♡, cherries & a little machine learning 🍒
</div>
""",
    unsafe_allow_html=True
)
