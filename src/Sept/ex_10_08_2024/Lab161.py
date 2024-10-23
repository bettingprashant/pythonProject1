#File handling

import os

full_path_file = os.path.join("C:\\Users\\91771\\OneDrive - SmartCare Analytica AB\\Desktop\\Python Automtion\\Python Selenium\\pythonProject1\\src\\Sept\\ex_10_08_2024\\pra", "raj.txt")

file = open(full_path_file, 'r')
content = file.read()

# open('pra/raj.txt', 'r')
# content = file.read()
print(content)