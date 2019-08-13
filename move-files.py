"""
This script takes a set of files from a text file, and line by line parses and
moves them to the corresponding directory.

It is used to move files in the website repo to the eds.org live website for the
time being. This script assumes that it is being run in the website repo.
"""

import os
import shutil
base_repo = "earthlab.github.io"
base_path = "~/"

# Open the text file and move files over to the other dir
fp = open('changed_files.txt', 'r')

# Loop through each file, clean the path and move to the final directory
for f in fp:
    print("Trying to move: ", f)
    f = f.rstrip('\n')
    f = f.strip()
    if not f.lower().endswith(('yml', 'py')):
        print("final file name: ", f)
        new_path = os.path.join(base_path, base_repo, f)
        dir_path = os.path.dirname(new_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        shutil.copy(f, new_path)
        print("File has been moved to: ", new_path)
    else:
        print("sorry can't move: ", f)




