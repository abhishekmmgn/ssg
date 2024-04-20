import os
import shutil

from copy_static import copy_files_recursive
from page_generation import generate_pages_recursive

DIR_PATH_STATIC = "./static"
DIR_PATH_DIST = "./dist"


def main():
    print("Deleting dist directory...")
    if os.path.exists(DIR_PATH_DIST):
        shutil.rmtree(DIR_PATH_DIST)

    print("Copying static files to dist directory...")
    copy_files_recursive(DIR_PATH_STATIC, DIR_PATH_DIST)

    generate_pages_recursive("./content", "./template.html", DIR_PATH_DIST)


main()
