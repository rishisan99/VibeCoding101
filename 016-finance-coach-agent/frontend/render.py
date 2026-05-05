import streamlit as st


def render_results(data: dict) -> None:
    recs = data.get("recommendations", {})
    if recs.get("message"):
        st.info(recs["message"])
    st.subheader("Budget Plan")
    st.write(recs.get("budget_plan", ""))
    st.subheader("Waste Detection")
    st.write(recs.get("waste_detection", ""))
    st.subheader("Monthly Targets")
    st.write(recs.get("monthly_targets", ""))
    st.subheader("Action Steps")
    for item in recs.get("action_steps", []):
        st.write(f"- {item}")
