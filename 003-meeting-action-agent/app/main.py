import streamlit as st

from app.ui import render_main, render_sidebar
from core.task_chain import run_task_chain


def main():
    st.set_page_config(page_title="Meeting Action Agent", layout="wide")

    api_key = render_sidebar()
    notes, run_clicked = render_main()
    st.subheader("Output")

    if not run_clicked:
        st.info("Task list will appear here after processing.")
        return

    if not api_key:
        st.error("Please add your OpenAI API key in the sidebar.")
        return
    if not notes.strip():
        st.warning("Please paste meeting notes first.")
        return

    with st.spinner("Processing notes..."):
        result = run_task_chain(api_key=api_key, notes=notes)
    if result["error"]:
        st.error(result["error"])
        return

    tasks = result["tasks"]
    if not tasks:
        st.info("No action items found in the notes.")
        return

    st.success("Tasks generated successfully.")
    st.table(tasks)
    with st.expander("Debug: Raw extracted actions"):
        st.code(result["raw_actions"] or "NO_ACTION_ITEMS")


if __name__ == "__main__":
    main()
