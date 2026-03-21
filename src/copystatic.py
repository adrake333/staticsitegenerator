import os
import shutil

def copy_static(src, dst):
    for item in os.listdir(src):
        full_path = os.path.join(src, item)
        print(full_path)
        if os.path.isfile(full_path):
            shutil.copy(full_path, dst)
        else:
            os.mkdir(os.path.join(dst, item))
            copy_static(full_path, os.path.join(dst, item))
