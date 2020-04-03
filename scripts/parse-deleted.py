'''
This script reads every line of "deleted_files.txt" and stores each line as an element in a list
From this list, we then parse out .ipynb files, .Rmd files, and image files (.jpg, .jpeg, .gif)
'''

with open("deleted_files.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


# Only run this stuff if there are changes!
if len(content) > 0:
    print("Looks like there are files to remove")
    deleted_md_files = [line for line in content if line.endswith(".md")]
    deleted_image_files = [line for line in content if line.endswith(".jpg") or line.endswith(".jpeg") or line.endswith(".gif") or line.endswith(".png")]

    if len(deleted_md_files) > 0:
        print("deleted posts: ", deleted_md_files)
        with open("deleted_md_files.txt", "w") as f:
            for fn in deleted_md_files:
                f.write("%s\n" % fn)

    if len(deleted_image_files) > 0:
        with open("deleted_image_files.txt", "w") as f:
            print("deleted image files: ", deleted_image_files)
            for fn in deleted_image_files:
                f.write("%s\n" % fn)

# Somehow deleted_files.txt is getting populated with empty values. Might be
# good to remove it to avoid cloning the website if there is nothing to move
# but this won't actually trigger a build unless there are things so maybe
# that's ok too.
