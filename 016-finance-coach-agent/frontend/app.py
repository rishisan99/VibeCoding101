import httpx
import streamlit as st

from frontend.client import request_plan
from frontend.render import render_results

st.set_page_config(page_title="Finance Coach", layout="wide")
st.title("Finance Coach Agent")
st.caption("Paste CSV, add goals, get guided money advice.")

with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("OpenAI API Key", type="password")
    spending_limit = st.number_input("Monthly spending limit", min_value=0.0)
    savings_target = st.number_input("Monthly savings target", min_value=0.0)
    focus_category = st.text_input("Focus category")
    month = st.text_input("Month")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
csv_text = st.text_area("Paste expense CSV", height=220)
input_csv = uploaded_file.getvalue().decode("utf-8") if uploaded_file else csv_text
goals = {
    "savings_target": savings_target,
    "spending_limit": spending_limit,
    "focus_category": focus_category,
    "month": month,
}

if st.button("Get Recommendations"):
    if not input_csv.strip():
        st.warning("Upload or paste a CSV first.")
    elif not any(goals.values()):
        st.warning("Add at least one goal.")
    else:
        try:
            result = request_plan(api_key, input_csv, goals)
            st.caption(f"Rows: {len(result.get('expenses', []))}")
            st.json(result.get("summary", {}))
            render_results(result)
        except httpx.HTTPStatusError as error:
            for item in error.response.json().get("detail", ["Request failed."]):
                st.error(item)
        except httpx.HTTPError:
            st.error("Could not reach the API. Start FastAPI first.")
