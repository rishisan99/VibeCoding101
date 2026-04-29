import streamlit as st

from app.ui.api import parse_resume, post_analysis

st.set_page_config(page_title="Job Application Agent", layout="wide")
st.title("Job Application Agent")
st.caption("Simple v1: one resume, one JD, one focused analysis.")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    st.caption("Paste your key here. It is only used for this analysis.")

resume_file = st.file_uploader("Upload resume", type=["pdf", "txt", "md"])
job_description = st.text_area("Paste job description", height=220)

if resume_file:
    try:
        with st.spinner("Reading your resume..."):
            parsed = parse_resume(resume_file)
        st.write("Parsed Resume Preview")
        st.text((parsed["resume_text"] or "")[:300] or "No text found.")
    except Exception as error:
        st.error(f"Could not read resume: {error}")

if st.button("Analyze", use_container_width=True):
    if not resume_file or not job_description.strip():
        st.warning("Please upload a resume and paste a job description first.")
    else:
        try:
            with st.spinner("Comparing resume with job description..."):
                data = post_analysis(api_key, job_description, resume_file)
            st.subheader(f"Fit Score: {data['fit_score']}")
            st.write("Resume Improvements")
            for item in data["resume_improvements"]:
                st.write(f"- {item}")
            st.write("Tailored Cover Letter")
            st.write(data["cover_letter"])
            st.write("Likely Interview Topics")
            for item in data["interview_topics"]:
                st.write(f"- {item}")
            st.write("Retrieved Resume Context")
            st.write(data["retrieved_context"])
            st.success("Analysis ready.")
        except Exception as error:
            st.error(f"Analysis failed: {error}")
else:
    st.info("Upload a resume and paste a JD to unlock analysis.")
