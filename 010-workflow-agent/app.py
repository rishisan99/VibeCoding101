import streamlit as st
from modules.agent import run_agent
from modules.sample_data import get_sample_workflow
from modules.ui import show_main_input, show_plan, show_results, show_sidebar, show_summary


st.set_page_config(page_title="Workflow Agent", layout="wide")
st.title("Workflow Agent")
st.caption("Paste a workflow. The agent will plan and run it step by step.")

api_key = show_sidebar()
if st.button("Load Sample Workflow"):
    st.session_state.workflow_text = get_sample_workflow()

workflow_text = show_main_input()
run_clicked = st.button("Run Agent", type="primary")

if api_key:
    st.success("API key added in sidebar.")

if run_clicked and not api_key:
    st.error("Add your OpenAI API key in the sidebar.")

if run_clicked and workflow_text and api_key:
    try:
        with st.spinner("Running agent..."):
            agent_output = run_agent(api_key, workflow_text)
        st.divider()
        show_plan(agent_output["steps"])
        show_summary(agent_output["summary"])
        show_results(agent_output["results"])
    except Exception as error:
        st.error(str(error))
