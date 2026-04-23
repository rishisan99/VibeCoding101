import streamlit as st
from modules.pipeline import transform_text
st.set_page_config(page_title="Content Repurpose Agent", layout="wide")
st.title("Content Repurpose Agent")
if "result_text" not in st.session_state:
    st.session_state["result_text"] = ""
with st.sidebar:
    st.header("Settings")
    st.text_input("OpenAI API Key", type="password", key="api_key", placeholder="sk-...")

left_col, right_col = st.columns(2)
with left_col:
    st.subheader("Input")
    st.text_area(
        "Paste your content",
        key="input_text",
        height=240,
        placeholder="Paste blog, mail, post, or any text here...",
        label_visibility="collapsed",
    )
with right_col:
    st.subheader("Output")
    st.text_area(
        "Generated output",
        value=st.session_state.get("result_text", ""),
        height=240,
        placeholder="Your transformed content will appear here...",
        label_visibility="collapsed",
    )
    st.code(st.session_state.get("result_text", "") or " ", language=None)

formats = ["blog", "mail", "post", "tweet", "script"]
sel_left, sel_right = st.columns(2)
with sel_left:
    st.selectbox("Input format", formats, key="input_format")
with sel_right:
    st.selectbox("Output format", formats, key="output_format")
api_key = st.session_state.get("api_key", "").strip()
if st.button("Run", key="run_btn", disabled=not api_key):
    source = st.session_state.get("input_text", "").strip()
    if not source:
        st.warning("Please add some input content.")
    else:
        try:
            st.session_state["result_text"] = transform_text(api_key, source, st.session_state["input_format"], st.session_state["output_format"])
            st.rerun()
        except Exception as e:
            st.error(f"Generation failed: {e}")
