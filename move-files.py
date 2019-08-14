"""
This script takes a set of files from a text file, and line by line parses and
moves them to the corresponding directory.

It is used to move files in the website repo to the eds.org live website for the
time being. This script assumes that it is being run in the website repo.
"""

import os
import shutil

# get absolute path
cwd = os.path.abspath(os.getcwd())
# create full path to other repo
eds_website_repo = cwd.replace("eds-lessons-website", "earthlab.github.io")

changed_files = "changed_files.txt"

# Open the text file and move files over to the other dir
fp = open(changed_files, 'r')

if os.stat(changed_files).st_size == 0:
    print("There are no changes to commit")
# Loop through each file, clean the path and move to the final directory
else:
    for f in fp:
        print("Trying to move: ", f)
        f = f.rstrip('\n').strip()
        if not f.lower().endswith(('yml', 'py')):
            print("final file name: ", f)
            new_path = os.path.join(eds_website_repo, f)
            dir_path = os.path.dirname(new_path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            shutil.copy(f, new_path)
            print("File has been moved to: ", new_path)
        else:
            print("sorry can't move: ", f)




