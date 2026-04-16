import streamlit as st


def render_section(title: str, items: list[str]) -> None:
    st.subheader(title)
    if not items:
        st.write("- None found")
        return
    for item in items:
        st.write(f"- {item}")


def render_insights(data: dict) -> None:
    """Render clean output sections."""
    render_section("Key Insights", data.get("key_insights", []))
    render_section("Risks", data.get("risks", []))
    render_section("Decisions", data.get("decisions", []))
    if data.get("raw"):
        st.caption("Raw model output:")
        st.code(data["raw"])
