import streamlit as st

from modules.openai_client import analyze_ticket_with_ai
from modules.triage import analyze_ticket


st.set_page_config(page_title="Support Triage Agent")

st.title("Support Triage Agent")
st.write("Paste a ticket to classify it and get a first response draft.")

samples = {
    "Blank": "",
    "Billing": "I was charged twice and need a refund.",
    "Login": "I cannot access my account after resetting my password.",
    "Bug": "The app crashes when I try to upload a file.",
}

choice = st.sidebar.selectbox("Sample ticket", samples)
api_key = st.sidebar.text_input("OpenAI API key", type="password")
mode = "OpenAI" if api_key else "Local rules"
st.sidebar.caption(f"Mode: {mode}")

ticket = st.text_area("Paste a support ticket", value=samples[choice], height=160)

if st.button("Analyze Ticket"):
    if not ticket:
        st.warning("Paste a ticket first.")
    else:
        result = analyze_ticket(ticket)

        if api_key:
            try:
                with st.spinner("Analyzing with OpenAI..."):
                    result = analyze_ticket_with_ai(ticket, api_key)
            except Exception as error:
                st.error(f"OpenAI failed, so local rules were used. {error}")

        st.subheader("Triage Result")
        col1, col2, col3 = st.columns(3)
        col1.metric("Category", result["category"])
        col2.metric("Priority", result["priority"])
        col3.metric("Team", result["team"])

        st.subheader("Suggested Response")
        st.info(result["response"])
