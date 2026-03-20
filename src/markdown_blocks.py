def markdown_to_blocks(markdown):
    blocks = []
    parts = markdown.split("\n\n")
    for each in parts:
        cleaned = each.strip()
        if len(cleaned) > 0:
            blocks.append(cleaned)
    return blocks
