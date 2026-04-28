import streamlit as st


def show_sidebar():
    with st.sidebar:
        st.header("Settings")
        st.text_input(
            "OpenAI API Key",
            type="password",
            key="openai_api_key",
            help="Paste your key here for this session.",
        )
    return st.session_state.get("openai_api_key", "").strip()


def show_main_input():
    # Keep the main input simple and easy to paste into.
    st.subheader("Workflow Input")
    st.caption("Example flow: email -> task -> summary")
    return st.text_area(
        "Describe the workflow",
        placeholder="Example: Read this email, make a task list, then write a short summary.",
        height=180,
        key="workflow_text",
    ).strip()


def show_plan(steps):
    st.subheader("Task List")
    for index, step in enumerate(steps, start=1):
        st.write(f"{index}. {step}")


def show_summary(summary_text):
    st.subheader("Summary")
    st.write(summary_text)


def show_results(results):
    st.subheader("Execution Log")
    for item in results:
        st.caption(item)
