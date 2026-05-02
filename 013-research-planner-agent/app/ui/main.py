import sys

import streamlit as st

from app.core.config import API_URL
from app.ui.client import request_plan
from app.ui.render import render_plan


def render() -> None:
    st.set_page_config(page_title="Research Planner", layout="wide")
    st.title("Research Planner")
    st.caption("Turn one topic into a simple research plan.")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    topic = st.text_area("Research Topic", placeholder="Example: AI agents in education")
    if st.button("Generate Plan", use_container_width=True):
        if not topic.strip() and not api_key:
            st.warning("Please add a topic and API key.")
            return
        if not topic.strip():
            st.warning("Please add a topic.")
            return
        if not api_key:
            st.warning("Please add your API key.")
            return
        try:
            render_plan(request_plan(API_URL, topic, api_key))
        except RuntimeError as exc:
            st.error(str(exc))


def run() -> None:
    from streamlit.web.cli import main

    sys.argv = ["streamlit", "run", __file__]
    raise SystemExit(main())


if __name__ == "__main__":
    render()
