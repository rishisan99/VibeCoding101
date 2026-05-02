# App Flow

1. User opens Streamlit app.
2. User pastes OpenAI API key in sidebar.
3. User enters a research topic in the main input.
4. Streamlit sends topic and key to FastAPI.
5. FastAPI runs planner behavior through LangGraph.
6. System returns:
   - research plan
   - search questions
   - source strategy
   - output template
7. Streamlit shows the result in simple sections.
