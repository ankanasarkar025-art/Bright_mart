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
    return pickle.load(open("linear_reg.sav", "rb"))

model = load_model()


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

/* ---------- GOOGLE FONT ---------- */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Pacifico&display=swap');

/* ---------- MAIN BACKGROUND ---------- */
.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.75) 0%, transparent 20%),
        radial-gradient(circle at 90% 80%, rgba(255,255,255,0.60) 0%, transparent 22%),
        linear-gradient(135deg, #fff5f7 0%, #ffe8ee 45%, #ffdce6 100%);
    font-family: 'DM Sans', sans-serif;
}

/* Remove top blank area */
.block-container {
    padding-top: 2.5rem;
    max-width: 720px;
}

/* ---------- DECORATIVE CHERRIES ---------- */

.cherry-left {
    position: fixed;
    top: 90px;
    left: 6%;
    font-size: 55px;
    transform: rotate(-15deg);
    opacity: 0.8;
    z-index: 0;
}

.cherry-right {
    position: fixed;
    bottom: 80px;
    right: 6%;
    font-size: 65px;
    transform: rotate(14deg);
    opacity: 0.8;
    z-index: 0;
}

.small-cherry {
    font-size: 25px;
    margin-bottom: 5px;
}


/* ---------- MAIN CARD ---------- */

.hero-card {
    background: rgba(255, 255, 255, 0.78);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1.5px solid rgba(255, 255, 255, 0.9);
    border-radius: 30px;
    padding: 32px 35px 22px 35px;
    margin-bottom: 25px;
    text-align: center;
    box-shadow:
        0 18px 45px rgba(190, 70, 105, 0.10),
        inset 0 1px 0 rgba(255,255,255,0.8);
}


/* ---------- TITLE ---------- */

.app-title {
    font-family: 'Pacifico', cursive;
    color: #c9365c;
    font-size: 44px;
    margin-bottom: 5px;
    line-height: 1.2;
}

.app-subtitle {
    color: #97566a;
    font-size: 16px;
    margin-top: 5px;
    margin-bottom: 10px;
}

.mini-text {
    display: inline-block;
    background: #ffe1e9;
    color: #b63b5b;
    border-radius: 50px;
    padding: 7px 16px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.3px;
    margin-top: 10px;
}


/* ---------- INPUT LABELS ---------- */

label {
    color: #842f49 !important;
    font-weight: 650 !important;
    font-size: 15px !important;
}


/* ---------- NUMBER INPUT ---------- */

div[data-baseweb="input"] {
    background-color: rgba(255,255,255,0.9) !important;
    border-radius: 15px !important;
    border: 1.5px solid #f5bacb !important;
    box-shadow: 0 5px 15px rgba(184, 67, 101, 0.05);
}

div[data-baseweb="input"]:focus-within {
    border: 1.5px solid #d94b70 !important;
    box-shadow: 0 0 0 3px rgba(217, 75, 112, 0.10);
}


/* ---------- PREDICT BUTTON ---------- */

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 16px;
    border: none;
    background: linear-gradient(135deg, #df4a70, #bd3156);
    color: white;
    font-size: 17px;
    font-weight: 700;
    box-shadow: 0 8px 20px rgba(190, 49, 86, 0.22);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #c9365c, #a92348);
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 12px 24px rgba(190, 49, 86, 0.28);
}

.stButton > button:active {
    transform: scale(0.98);
}


/* ---------- INPUT SECTION ---------- */

.section-title {
    font-size: 18px;
    color: #92334f;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 12px;
}


/* ---------- RESULT CARD ---------- */

.result-card {
    margin-top: 22px;
    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.95),
        rgba(255,225,233,0.95)
    );
    border: 2px solid #f7b4c7;
    border-radius: 24px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 12px 30px rgba(184, 67, 101, 0.12);
}

.result-label {
    color: #96546a;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 2px;
}

.result-number {
    color: #c52f58;
    font-size: 46px;
    font-weight: 800;
    margin: 3px 0;
}

.result-note {
    color: #aa6579;
    font-size: 13px;
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #ba7c8d;
    font-size: 12px;
    margin-top: 35px;
    padding-bottom: 10px;
}


/* Hide Streamlit default menu/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# DECORATIVE CHERRIES
# --------------------------------------------------
st.markdown("""
<div class="cherry-left">🍒</div>
<div class="cherry-right">🍒</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown("""
<div class="hero-card">

    <div class="small-cherry">🍒</div>

    <div class="app-title">
        Cherry Sales
    </div>

    <div class="app-subtitle">
        Turn your advertising budget into a sweet little sales forecast.
    </div>

    <span class="mini-text">
        ✨ Powered by Machine Learning
    </span>

</div>
""", unsafe_allow_html=True)


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
    step=1.0,
    help="Enter the amount spent on TV advertising."
)

Radio = st.number_input(
    "🎧 Radio Advertising Budget",
    min_value=0.0,
    value=0.0,
    step=1.0,
    help="Enter the amount spent on Radio advertising."
)

Newspaper = st.number_input(
    "📰 Newspaper Advertising Budget",
    min_value=0.0,
    value=0.0,
    step=1.0,
    help="Enter the amount spent on Newspaper advertising."
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

            <div style="font-size:32px;">🍒</div>

            <div class="result-label">
                YOUR PREDICTED SALES
            </div>

            <div class="result-number">
                {prediction:.2f}
            </div>

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
st.markdown("""
<div class="footer">
    made with ♡, cherries & a little machine learning 🍒
</div>
""", unsafe_allow_html=True)
