import streamlit as st


def render_upload():
    st.write("Upload at least 2 contracts to compare risk, missing clauses, and inconsistencies.")
    files = st.file_uploader(
        "Upload contracts",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True,
    )
    if files:
        st.caption(", ".join(file.name for file in files))
    clicked = st.button("Analyze Contracts", use_container_width=True)
    return files, clicked
