import streamlit as st


def show_overview(df, patterns):
    st.subheader("Insights")
    c1, c2 = st.columns(2)
    c1.metric("Total spend", f"{patterns['total_spend']:.2f}")
    c2.metric("Transactions", len(df))
    st.write("Top categories")
    st.dataframe(patterns["by_category"], use_container_width=True)
    st.write("Recurring expenses")
    if patterns["recurring"].empty:
        st.info("No recurring descriptions found.")
    else:
        st.dataframe(patterns["recurring"], use_container_width=True)
    st.write("Unusual expenses")
    if patterns["unusual"].empty:
        st.info("No unusual expenses found.")
    else:
        st.dataframe(patterns["unusual"], use_container_width=True)


def show_recommendations(recs):
    st.subheader("Recommendations")
    st.write(recs["llm"])
