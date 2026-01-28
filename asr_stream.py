def stream_asr(audio_stream):
    partials = [
        "How do I reset the router",
        "How do I reset the router and what about",
        "How do I reset the router and what about the second one"
    ]
    for p in partials:
        yield p
