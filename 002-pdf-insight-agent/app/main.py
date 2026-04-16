import streamlit as st

from core import run_rag_pipeline
from ui import render_insights, render_sidebar


def main() -> None:
    st.set_page_config(page_title="PDF Insight Agent", layout="wide")
    st.title("PDF Insight Agent")
    st.write("Upload a PDF and extract key insights, risks, and decisions.")

    ui_state = render_sidebar()
    st.write(f"API key added: {bool(ui_state['api_key'])}")
    st.write(f"PDF uploaded: {ui_state['uploaded_file'] is not None}")

    if not ui_state["run_analysis"]:
        return
    if not ui_state["api_key"]:
        st.warning("Paste your OpenAI API key in the sidebar.")
        return
    if ui_state["uploaded_file"] is None:
        st.warning("Upload a PDF to run analysis.")
        return

    with st.spinner("Running RAG pipeline..."):
        result = run_rag_pipeline(ui_state["uploaded_file"], ui_state["api_key"])

    pages = result["pages"]
    chunks = result["chunks"]
    hits = result["hits"]
    st.write(f"Pages: {len(pages)} | Chunks: {len(chunks)} | Retrieved: {len(hits)}")
    if result.get("error"):
        st.error(result["error"])
        return
    render_insights(result["insights"])


if __name__ == "__main__":
    main()
