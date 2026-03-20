from enum import Enum

def markdown_to_blocks(markdown):
    blocks = []
    parts = markdown.split("\n\n")
    for each in parts:
        cleaned = each.strip()
        if len(cleaned) > 0:
            blocks.append(cleaned)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    num_hashes = len(block) - len(block.lstrip("#"))
    if 1 <= num_hashes <= 6 and len(block) > num_hashes and block[num_hashes] == " ":
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    else:
        for i, line in enumerate(lines, start=1):
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

