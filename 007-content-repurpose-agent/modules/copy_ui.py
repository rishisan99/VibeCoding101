import json
import streamlit.components.v1 as components


def render_copy_button(text: str) -> None:
    safe_text = json.dumps(text or "")
    html = f"""
    <button onclick='copyText()'
      style="font-size:12px;padding:4px 10px;border:1px solid #ccc;border-radius:6px;background:#f7f7f7;cursor:pointer;">
      Copy
    </button>
    <script>
      function copyText() {{
        navigator.clipboard.writeText({safe_text});
      }}
    </script>
    """
    components.html(html, height=36)
