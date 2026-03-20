from enum import Enum
from htmlnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from split_delimiter import text_to_textnodes

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

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        chlidren.append(html_node)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType. ORDERED_LIST:
        return ordered_list_to_html_node(block)
    raise ValueError("unrecognized block type")

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    children = text_to_children(block[level + 1:])
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    text_node = TextNode(block[3:-3], TextType.TEXT)
    child = text_node_to_html_node(text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.lstrip(">").strip())
    joined_lines = " ".join(stripped_lines)
    children = text_to_children(joined_lines)
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    parent_list = []
    for line in lines:
        stripped_line = line.lstrip("-").strip()
        children = text_to_children(stripped_line)
        parent_list.append(ParentNode("li", children))
    return ParentNode("ul", parent_list)

def ordered_list_to_html_node(block):
    lines = block.split("\n")
    parent_list = []
    for line in lines:
        text = line.split(". ", 1)[1]
        children = text_to_children(text)
        parent_list.append(ParentNode("li", children))
    return ParentNode("ol", parent_list)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes
