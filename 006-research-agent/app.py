"""Streamlit entry point."""

import streamlit as st

from agent import run_research
from utils import has_api_key

st.set_page_config(page_title="Simple Research Agent")
st.title("Simple Research Agent")
st.caption("Search the web and get a short summary.")

st.sidebar.header("Settings")
api_key = st.sidebar.text_input(
    "Paste OpenAI API Key",
    type="password",
    placeholder="sk-...",
)
query = st.text_input("Research topic", placeholder="Example: latest AI coding agents")

if st.button("Research"):
    if not has_api_key(api_key):
        st.error("Please paste your OpenAI API key in the sidebar.")
    elif not query.strip():
        st.warning("Please enter a topic.")
    else:
        try:
            with st.spinner("Researching..."):
                result = run_research(query=query, api_key=api_key)
        except Exception as err:
            st.error(f"Research failed: {err}")
        else:
            st.subheader("Summary")
            st.write(result.get("summary", "No summary returned."))
            st.subheader("Sources")
            sources = result.get("sources", [])
            if not sources:
                st.info("No source links found.")
            for i, source in enumerate(sources, start=1):
                st.markdown(f"{i}. [{source['title']}]({source['url']})")
