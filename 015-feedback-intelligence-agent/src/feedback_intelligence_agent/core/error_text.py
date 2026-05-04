def user_error_text(error: Exception) -> str:
    text = str(error).strip()
    if text:
        return text
    return error.__class__.__name__
