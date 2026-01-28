def rewrite_query(partial_text, chat_history):
    if "second one" in partial_text.lower():
        return f"Explain step 2 of: {chat_history[-1]}"
    return partial_text
