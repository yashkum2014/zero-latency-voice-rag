def llm_stream(prompt):
    filler = "Let me check the technical manual for that."
    yield filler

    final_answer = (
        "First, unplug the router. "
        "Wait ten seconds. "
        "Plug it back in. "
        "The second step confirms the reset."
    )

    for token in final_answer.split():
        yield token + " "
