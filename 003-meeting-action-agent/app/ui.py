import streamlit as st

SAMPLE_NOTES = """Alice: finalize landing page copy by Friday.
Bob: share pricing deck with sales by Apr 25.
Team: schedule customer interview next week."""


def render_sidebar():
    """Sidebar with OpenAI API key input."""
    st.sidebar.header("Settings")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    if api_key:
        st.sidebar.success("API key added for this session.")
    return api_key


def render_main():
    """Main page skeleton for notes to tasks."""
    st.title("Meeting Action Agent")
    st.write("Paste meeting notes and click run.")
    with st.expander("Sample notes for quick test"):
        st.code(SAMPLE_NOTES)

    use_sample = st.checkbox("Use sample notes")
    default_notes = SAMPLE_NOTES if use_sample else ""
    notes = st.text_area(
        "Meeting Notes",
        value=default_notes,
        height=220,
        placeholder="Paste notes...",
    )
    run_clicked = st.button("Run")
    return notes, run_clicked
