def analyze_ticket(ticket):
    text = ticket.lower()
    category = get_category(text)
    return {
        "category": category,
        "priority": get_priority(text),
        "team": get_team(category),
        "response": get_response(category),
    }


def get_category(text):
    if has_any(text, ["refund", "invoice", "payment", "charged"]):
        return "Billing"
    if has_any(text, ["login", "password", "account", "access"]):
        return "Account Access"
    if has_any(text, ["bug", "error", "crash", "not working"]):
        return "Technical Issue"
    if has_any(text, ["feature", "request", "improve", "add"]):
        return "Feature Request"
    return "General Support"


def get_priority(text):
    if has_any(text, ["urgent", "down", "blocked", "cannot use", "critical"]):
        return "High"
    if has_any(text, ["issue", "problem", "error", "delayed"]):
        return "Medium"
    return "Low"


def get_team(category):
    teams = {
        "Billing": "Finance Support",
        "Account Access": "Account Support",
        "Technical Issue": "Engineering Support",
        "Feature Request": "Product Team",
    }
    return teams.get(category, "Customer Support")


def get_response(category):
    return (
        f"Thanks for reaching out. We identified this as a {category.lower()} "
        "ticket. Our team will review it and follow up with next steps soon."
    )

def has_any(text, words):
    return any(word in text for word in words)
