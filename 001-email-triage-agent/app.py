"""Simple Streamlit UI for email triage."""

import streamlit as st

from agent import triage_email

st.set_page_config(page_title="Email Triage Agent", layout="wide")
st.title("Email Triage Agent")
st.caption("Classify emails, extract actions, and draft replies.")
result = None

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    if api_key:
        st.success("API key added for this session.")
    else:
        st.info("Paste your API key. It is used only for this run.")

st.subheader("Email Input")
email_text = st.text_area(
    "Paste email text",
    height=260,
    placeholder="Hi team, can we ship this by Friday?...",
)

if st.button("Analyze Email", type="primary"):
    if not api_key:
        st.error("Please paste your OpenAI API key in the sidebar.")
    elif not email_text.strip():
        st.error("Please paste email text.")
    else:
        with st.spinner("Analyzing email..."):
            result = triage_email(api_key=api_key.strip(), email_text=email_text.strip())

st.subheader("Output JSON")
if result:
    st.json(result)
    if "error" in result:
        st.warning(result["error"])
else:
    st.code(
        '{"priority":"urgent|action|fyi","summary":"","action_items":[],"reply_draft":""}',
        language="json",
    )
