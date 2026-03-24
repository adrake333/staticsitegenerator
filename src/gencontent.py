import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("invalid markdown - no h1")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        read_from = f.read()
    with open(template_path) as f:
        read_template = f.read()
    html_node = markdown_to_html_node(read_from)
    html_string = html_node.to_html()
    title = extract_title(read_from)
    new_content = read_template.replace("{{ Content }}", html_string)
    new_template = new_content.replace("{{ Title }}", title)    
    parent_dir = os.path.dirname(dest_path)
    if parent_dir and not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)
    with open(dest_path, "w") as f:
        f.write(new_template)
