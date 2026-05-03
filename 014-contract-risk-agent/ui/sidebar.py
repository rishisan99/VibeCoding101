import streamlit as st


def render_sidebar(api_ok: bool) -> str:
    with st.sidebar:
        st.header("Settings")
        st.caption("Backend: online" if api_ok else "Backend: offline")
        return st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-...",
        )
