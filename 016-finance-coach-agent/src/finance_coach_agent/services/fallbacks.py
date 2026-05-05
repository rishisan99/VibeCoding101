def fallback_advice(message: str) -> dict:
    return {
        "budget_plan": "No plan yet.",
        "waste_detection": "No waste check yet.",
        "monthly_targets": "No target set yet.",
        "action_steps": [message],
        "message": message,
    }
