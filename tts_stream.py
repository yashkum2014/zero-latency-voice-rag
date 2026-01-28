def stream_tts(text_stream):
    for chunk in text_stream:
        print(f"[AUDIO]: {chunk}")
