


import os
import shutil
base_repo = "dummy-website-test"
base_path = "~/"
#base_path = "../"


# Open the text file and move files over to the other dir
fp = open('changed_files.txt', 'r')
print("here is the file: ", fp)

os.getcwd()

for f in fp:
    print("Trying to move: ", f)
    if not f.lower().endswith(('yml', 'py')):
        f = f.rstrip('\n')
        print("final file name: ", f)
        new_path = os.path.join(base_path, base_repo, f)
        dir_path = os.path.dirname(new_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        print("moving to: ", new_path)
        shutil.copy(f, new_path)








