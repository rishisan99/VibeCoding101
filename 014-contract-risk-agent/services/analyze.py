from core.postprocess import clean_result
from core.validate import validate_files
from core.vectorstore import drop_collection
from graph import contract_graph
from models import AnalysisResult


def analyze_contracts(files: list[dict], api_key: str) -> AnalysisResult:
    validate_files(files)
    state = contract_graph.invoke({"files": files, "api_key": api_key})
    try:
        return clean_result(state["result"])
    finally:
        if state.get("collection"):
            drop_collection(state["collection"])
