def create_jellyfin_message_context(context: dict):
    runtime = context.get("RunTime")
    if runtime:
        parts = runtime.split(":")
        seconds = parts.pop()
        minutes = f"{int(parts.pop())}m"
        hours = ""
        if parts:
            hours = f"{int(parts.pop())}h"
        cleaned_runtime = f"{hours}{minutes}"
        context["RunTime"] = cleaned_runtime

    subtitles = set()
    for key in context.keys():
        if key.startswith("Subtitle") and key.endswith("Language"):
            subtitles.add(context[key])
    context["Subtitles"] = ", ".join(list(subtitles))

    audio = set()
    for key in context.keys():
        if key.startswith("Subtitle") and key.endswith("Language"):
            audio.add(context[key])
    context["Audio"] = ", ".join(list(audio))
    return context
