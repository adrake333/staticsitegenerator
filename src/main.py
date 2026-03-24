import os
import shutil
from copystatic import copy_static
from gencontent import generate_page

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    copy_static("static", "public")

main()
