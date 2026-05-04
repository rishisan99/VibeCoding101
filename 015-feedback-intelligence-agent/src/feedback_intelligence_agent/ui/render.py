import streamlit as st


def render_list(title: str, items: list[str]) -> None:
    st.subheader(title)
    for item in items:
        st.write(f"- {item}")


def render_result(result: dict) -> None:
    st.caption(f"Flow: {result['flow']}")
    st.write(f"Feedback items: {result['total_items']}")
    col1, col2 = st.columns(2)
    with col1:
        render_list("Themes", result["themes"])
        render_list("Urgent Issues", result["urgent_issues"])
    with col2:
        st.subheader("Sentiment")
        st.write(result["sentiment"])
        render_list("Feature Requests", result["feature_requests"])
