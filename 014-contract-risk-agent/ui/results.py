import streamlit as st


def show_clause_block(title: str, items: list[dict], key: str) -> None:
    st.subheader(title)
    if not items:
        st.info(f"No {key} yet.")
    for item in items:
        st.write(f"**{item.get('clause', item.get('point'))}**")
        if item.get("contract"):
            st.caption(item["contract"])
        st.write(item["reason"])


def render_results(data: dict) -> None:
    st.success("Analysis complete")
    show_clause_block("Risky Clauses", data["risky_clauses"], "risky clauses")
    show_clause_block("Missing Clauses", data["missing_clauses"], "missing clauses")
    st.subheader("Inconsistencies")
    for item in data["inconsistencies"]:
        st.write(f"**{item['point']}**")
        st.write(", ".join(item["contracts"]) or "No contracts")
        st.write(item["reason"])
    st.subheader("Cross-Document Reasoning")
    for line in data["cross_document_reasoning"]:
        st.write(f"- {line}")
    st.subheader("Final Summary")
    st.write(data["final_summary"])
