import requests
import streamlit as st

from config import PAGE_TITLE
from ui.client import api_ready, send_analysis
from ui.results import render_results
from ui.sidebar import render_sidebar
from ui.upload import render_upload

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
api_key = render_sidebar(api_ready())
files, clicked = render_upload()

if clicked:
    if not api_key:
        st.warning("Add the OpenAI API key.")
    elif not files or len(files) < 2:
        st.warning("Upload at least 2 contracts.")
    else:
        try:
            with st.spinner("Reviewing contracts..."):
                render_results(send_analysis(api_key, files))
        except requests.RequestException:
            st.error("Could not reach the backend. Start FastAPI and try again.")
        except ValueError as exc:
            st.error(str(exc))
