import streamlit as st


def render_sidebar() -> dict:
    """Render sidebar controls for API key and PDF upload."""
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your key here",
        )
        uploaded_file = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
            accept_multiple_files=False,
        )
        run_analysis = st.button("Run Analysis", use_container_width=True)

    return {
        "api_key": api_key.strip(),
        "uploaded_file": uploaded_file,
        "run_analysis": run_analysis,
    }
