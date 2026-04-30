import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="Lead Qualification Agent")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Paste OpenAI API Key", type="password")
st.title("Lead Qualification Agent")
st.caption("Classify leads into hot, warm, or cold.")

with st.form("lead_form"):
    data = {k: st.text_input(k.replace("_", " ").title()) for k in [
        "lead_name", "lead_role", "company_name", "company_industry",
        "company_size", "lead_source",
    ]}
    data["lead_notes"] = st.text_area("Lead Notes")
    submitted = st.form_submit_button("Analyze")

if submitted:
    if not api_key:
        st.error("Paste your OpenAI API key in the sidebar.")
    else:
        try:
            response = requests.post(API_URL, json=data, headers={"x-api-key": api_key}, timeout=60)
            if response.ok:
                result = response.json()
                st.subheader(f"Priority: {result['priority']} ({result['score']})")
                st.write("Why:", result["why"])
                st.write("Next action:", result["next_action"])
                st.text_area("CRM Summary", result["crm_summary"], height=120)
            else:
                st.error(response.text)
        except requests.RequestException:
            st.error("Backend is not running on port 8000.")
