import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("invalid markdown - no h1")

def generate_page(from_path, template_path, dest_path, basepath):
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
    new_template_2 = new_template.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    parent_dir = os.path.dirname(dest_path)
    if parent_dir and not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)
    with open(dest_path, "w") as f:
        f.write(new_template_2)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_path) and full_path.endswith(".md"):
            html_name = entry.replace(".md", ".html")
            dest_path = os.path.join(dest_dir_path, html_name)
            generate_page(full_path, template_path, dest_path, basepath)
        elif os.path.isdir(full_path):
            next_dest = os.path.join(dest_dir_path, entry)
            if not os.path.exists(next_dest):
                os.mkdir(next_dest)
            generate_pages_recursive(full_path, template_path, next_dest, basepath)
            
