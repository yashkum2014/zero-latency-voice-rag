def voice_optimize(text):
    replacements = {
        "initialize": "start",
        "configuration": "settings"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)

    sentences = text.split(".")
    return ". ".join(s.strip() for s in sentences if s)
