import streamlit as st
from modules.csv_loader import load_csv, preview_data
from modules.categorizer import categorize_expenses
from modules.patterns import detect_patterns
from modules.recommendations import build_recommendations
from app.ui_sections import show_overview, show_recommendations

st.set_page_config(page_title="Expense Intelligence Agent", layout="wide")
st.title("Expense Intelligence Agent")
st.caption("Upload a CSV and get insights + savings recommendations")

st.sidebar.header("Settings")
api_key = st.sidebar.text_input("OpenAI API key", type="password")
uploaded = st.sidebar.file_uploader("Choose expense CSV", type=["csv"])

if uploaded is None:
    st.info("Upload your CSV and enter API key to start analysis.")
elif not api_key:
    st.info("Upload your CSV and enter API key to start analysis.")
else:
    try:
        st.info("Analyzing your expenses and generating insights...")
        with st.spinner("Getting insights..."):
            df = load_csv(uploaded)
            df = categorize_expenses(df, api_key)
            patterns = detect_patterns(df)
            recs = build_recommendations(df, api_key)
        st.subheader("Data Preview")
        st.dataframe(preview_data(df, 10), use_container_width=True)
        show_overview(df, patterns)
        show_recommendations(recs)
    except Exception as err:
        st.error(f"Could not process CSV: {err}")

st.sidebar.caption("Run: uv run streamlit run app/main.py")
