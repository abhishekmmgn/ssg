import os
import shutil

from copy_static import copy_files_recursive
from page_generation import generate_pages_recursive

dir_path_static = "./static"
dir_path_dist = "./dist"


def main():
    print("Deleting dist directory...")
    if os.path.exists(dir_path_dist):
        shutil.rmtree(dir_path_dist)

    print("Copying static files to dist directory...")
    copy_files_recursive(dir_path_static, dir_path_dist)

    generate_pages_recursive("./content", "./template.html", dir_path_dist)


main()
