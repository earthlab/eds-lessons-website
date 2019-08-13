


import os
import shutil
base_repo = "dummy-website-test"
base_path = "~/"
#base_path = "../"

print("Now doing stuff")
print("Now doing stuff")

# Open the text file and move files over to the other dir
fp = open('changed-files.txt', 'r')

for f in fp:
    print(f)
    if not f.lower().endswith(('.yml')):
        print(f)
        new_path = os.path.join(base_path, base_repo, f)
        dir_path = os.path.dirname(new_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        print(new_path)
        shutil.copy(f, new_path)








