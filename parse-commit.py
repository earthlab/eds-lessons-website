'''
This script reads every line of "changed_files.txt" and extracts only the files
that should be moved to the live website.
'''

with open("changed_files.txt") as f:
    content = f.readlines()
content = [x.rstrip('\n').strip() for x in content]


website_files = [line for line in content if not line.endswith((".py", "yml"))]

with open("website_files.txt", "w") as f:
    if len(website_files) > 0:
        for fn in website_files:
            f.write("%s\n" % fn)
