import os

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("invalid markdown - no h1")

def generate_page(from_path, template_path, dest_path):
