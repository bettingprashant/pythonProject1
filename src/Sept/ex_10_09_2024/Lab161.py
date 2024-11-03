#File handling

import os

full_path_file = os.path.join("/src/Sept/ex_10_09_2024\\pra", "raj.txt")

file = open(full_path_file, 'r')
content = file.read()

# open('pra/raj.txt', 'r')
# content = file.read()
print(content)