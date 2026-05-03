SYSTEM_PROMPT = """
You are an experienced contract review expert focused on commercial service agreements, legal risk analysis, and cross-document comparison.
Use only the provided text.
Do not invent missing facts.
Be conservative. Do not call a clause risky unless the risk is clear from the wording.
Common clauses are not risky by default.
Keep reasons short and simple.
""".strip()


def build_compare_prompt(names: list[str], context: str) -> str:
    return f"Contracts: {', '.join(names)}\nFind only meaningful inconsistencies across contracts. Focus on payment, term, termination, liability, confidentiality, indemnity, and disputes. Ignore minor wording changes.\n\n{context}"


def build_risk_prompt(names: list[str], context: str) -> str:
    return f"Contracts: {', '.join(names)}\nFind only clearly risky clauses. Do not flag normal market clauses just because they favor one side a little. Flag vague duties, one-sided rights, uncapped or broad liability, missing mutuality, short cure or notice, or unclear payment risk. Return clause, reason, contract.\n\n{context}"


def build_missing_prompt(names: list[str], context: str) -> str:
    return f"Contracts: {', '.join(names)}\nFind clauses that are clearly missing or too weak for this kind of service contract. Do not list optional clauses unless their absence creates a real gap. Prefer disputes, confidentiality, liability, payment, scope, term, termination, and renewal only when justified by the text. Return clause, reason, contract.\n\n{context}"


def build_summary_prompt(data: str) -> str:
    return f"Write a short final summary. Emphasize the strongest risks first. Do not overstate uncertain points.\n\n{data}"
