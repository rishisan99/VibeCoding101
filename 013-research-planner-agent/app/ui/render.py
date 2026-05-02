import streamlit as st


def render_plan(data: dict) -> None:
    st.subheader("Research Plan")
    st.write(data["research_plan"])
    st.subheader("Search Questions")
    for question in data["search_questions"]:
        st.write(f"- {question}")
    st.subheader("Source Strategy")
    st.write(data["source_strategy"])
    st.subheader("Output Template")
    st.code(data["output_template"])
