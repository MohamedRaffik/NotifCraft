def build_context(context: dict):
    content: str = context.get("message")
    if ":" in content:
        last_index = 0
        for i in range(len(content) - 1, -1, -1):
            if content[i] == ":":
                last_index = i
                break
        media = content[:last_index]
        message = content[last_index + 1 :]
        return {"media": media.strip(), "message": message.strip()}
    return {"media": context.get("title"), "message": context.get("message")}


print(build_context({"message": "Aquaman (2023) : English Subtitles DOwnloads"}))
