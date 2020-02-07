'''
This script reads every line of "deleted_files.txt" and stores each line as an element in a list
From this list, we then parse out .ipynb files, .Rmd files, and image files (.jpg, .jpeg, .gif)
'''

with open("deleted_files.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

deleted_md_files = [line for line in content if line.endswith(".md")]
deleted_image_files = [line for line in content if line.endswith(".jpg") or line.endswith(".jpeg") or line.endswith(".gif") or line.endswith(".png")]

print("deleted notebooks: ", deleted_notebooks)
print("deleted image files: ", deleted_image_files)


with open("deleted_notebooks.txt", "w") as f:
    if len(deleted_notebooks) > 0:
        for fn in deleted_notebooks:
            f.write("%s\n" % fn)

with open("deleted_image_files.txt", "w") as f:
    if len(deleted_image_files) > 0:
        for fn in deleted_image_files:
            f.write("%s\n" % fn)
