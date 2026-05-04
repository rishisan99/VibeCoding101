import streamlit as st

from feedback_intelligence_agent.core.dataset import load_latest_feedback
from feedback_intelligence_agent.core.flow import FLOW_STEPS
from feedback_intelligence_agent.ui.client import call_analyze_api
from feedback_intelligence_agent.ui.render import render_result

st.set_page_config(page_title="Feedback Intelligence", layout="wide")
st.title("Feedback Intelligence Agent")

if "feedback_text" not in st.session_state:
    st.session_state["feedback_text"] = load_latest_feedback()

api_key = st.sidebar.text_input("OpenAI API Key", type="password")
api_url = st.sidebar.text_input("FastAPI URL", "http://127.0.0.1:8000")
if st.sidebar.button("Load Last Dataset"):
    st.session_state["feedback_text"] = load_latest_feedback()
st.sidebar.caption("Paste your key here for local testing.")

feedback = st.text_area("Paste reviews or comments", height=220, key="feedback_text")
st.subheader("Planned Flow")
for step in FLOW_STEPS:
    st.write(f"- {step}")

if st.button("Analyze", disabled=not feedback.strip()):
    try:
        result = call_analyze_api(api_url, feedback, api_key)
        render_result(result.model_dump())
    except Exception as error:
        st.error(str(error))

if api_key:
    st.success("API key captured in the sidebar.")
