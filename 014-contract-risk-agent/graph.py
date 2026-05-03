from typing import TypedDict
from langgraph.graph import END, START, StateGraph
from core.llm import run_structured
from core.loader import load_contracts
from core.prompts import build_compare_prompt, build_missing_prompt, build_risk_prompt, build_summary_prompt
from core.retriever import build_contexts
from core.splitter import build_chunks
from core.validate import filter_docs, validate_chunks
from core.vectorstore import build_collection
from models import AnalysisResult, CompareReview, MissingReview, RiskReview, SummaryReview
class GraphState(TypedDict, total=False):
    api_key: str
    files: list[dict]
    docs: list[dict]
    chunks: list[dict]
    collection: str
    contexts: dict[str, str]
    compare: CompareReview; risk: RiskReview
    missing: MissingReview; summary: SummaryReview
    result: AnalysisResult
def ingest(state: GraphState) -> GraphState:
    docs = filter_docs(load_contracts(state["files"]))
    chunks = build_chunks(docs)
    validate_chunks(chunks)
    return {"docs": docs, "chunks": chunks}
def index_docs(state: GraphState) -> GraphState:
    return {"collection": build_collection(state["chunks"], state["api_key"])}
def retrieve(state: GraphState) -> GraphState:
    names = [doc["name"] for doc in state["docs"]]
    return {"contexts": build_contexts(state["collection"], state["api_key"], names)}
def compare(state: GraphState) -> GraphState:
    names = [doc["name"] for doc in state["docs"]]
    return {"compare": run_structured(CompareReview, build_compare_prompt(names, state["contexts"]["compare"]), state["api_key"])}
def risk(state: GraphState) -> GraphState:
    names = [doc["name"] for doc in state["docs"]]
    return {"risk": run_structured(RiskReview, build_risk_prompt(names, state["contexts"]["risk"]), state["api_key"])}
def missing(state: GraphState) -> GraphState:
    names = [doc["name"] for doc in state["docs"]]
    return {"missing": run_structured(MissingReview, build_missing_prompt(names, state["contexts"]["missing"]), state["api_key"])}
def summarize(state: GraphState) -> GraphState:
    text = str({"risk": state["risk"], "missing": state["missing"], "compare": state["compare"]})
    return {"summary": run_structured(SummaryReview, build_summary_prompt(text), state["api_key"])}
def finalize(state: GraphState) -> GraphState:
    return {"result": AnalysisResult(risky_clauses=state["risk"].risky_clauses, missing_clauses=state["missing"].missing_clauses, inconsistencies=state["compare"].inconsistencies, cross_document_reasoning=state["compare"].cross_document_reasoning, final_summary=state["summary"].final_summary)}
graph = StateGraph(GraphState)
for name, fn in [("ingest", ingest), ("index_docs", index_docs), ("retrieve", retrieve), ("compare", compare), ("risk", risk), ("missing", missing), ("summarize", summarize), ("finalize", finalize)]:
    graph.add_node(name, fn)
for start, end in [(START, "ingest"), ("ingest", "index_docs"), ("index_docs", "retrieve"), ("retrieve", "compare"), ("compare", "risk"), ("risk", "missing"), ("missing", "summarize"), ("summarize", "finalize"), ("finalize", END)]:
    graph.add_edge(start, end)
contract_graph = graph.compile()
