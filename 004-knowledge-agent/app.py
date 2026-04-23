import streamlit as st

from knowledge_agent.pipeline import answer_question

st.set_page_config(page_title="Knowledge Agent", page_icon="📚", layout="wide")
st.sidebar.title("Settings")
st.session_state["api_key"] = st.sidebar.text_input(
    "OpenAI API Key",
    type="password",
    help="This key is read from the frontend sidebar for this session.",
).strip()

st.title("📚 Personal Knowledge Agent")
st.caption("Ask questions over notes and PDFs")

notes = st.text_area("Paste notes", height=180)
files = st.file_uploader(
    "Upload files (.txt, .md, .pdf)",
    type=["txt", "md", "pdf"],
    accept_multiple_files=True,
)
question = st.text_input("Ask a question")

if st.button("Ask"):
    if not st.session_state["api_key"]:
        st.error("Please paste your OpenAI API key in the sidebar.")
    elif not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                answer = answer_question(
                    question=question,
                    api_key=st.session_state["api_key"],
                    pasted_notes=notes,
                    uploaded_files=files,
                )
                st.write(answer)
            except Exception as err:
                st.error(f"Error: {err}")
