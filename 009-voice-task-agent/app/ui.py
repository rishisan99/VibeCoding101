import streamlit as st

from app.service import run_pipeline


def show_home() -> None:
    st.set_page_config(page_title="Voice Task Agent", layout="centered")
    st.title("Voice Notes to Tasks")
    st.caption("Speech to tasks with a simple voice pipeline.")
    st.sidebar.title("Settings")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    audio_file = st.file_uploader("Upload a voice note", type=["mp3", "wav", "m4a"])
    if audio_file:
        st.audio(audio_file)
    if st.button("Convert to Tasks", use_container_width=True):
        if not api_key:
            st.error("Please paste your OpenAI API key in the sidebar.")
            return
        if not audio_file:
            st.error("Please upload a voice note first.")
            return
        try:
            with st.spinner("Turning speech into tasks..."):
                transcript, tasks = run_pipeline(api_key, audio_file)
        except Exception as error:
            st.error(f"Something went wrong: {error}")
            return
        st.subheader("Transcript")
        st.write(transcript)
        st.subheader("Tasks")
        if not tasks:
            st.info("No clear tasks found in this voice note.")
        for index, task in enumerate(tasks, start=1):
            st.write(f"{index}. {task}")
