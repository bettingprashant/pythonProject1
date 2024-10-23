import os
#
# print(os.name)
# if os.name == 'nt':
#     print("using Windos")
# else:
#     print("mac")
#
# print(os.getcwd())
# os.chdir("C:\\Users\\91771\\Downloads\\Website_DataMetricks")
# os.mkdir('new_directory')
# os.makedirs('parent/child/grandchild')
# print(os.listdir('.'))
# for file in os.listdir('.'):
#     print(file)
# os.remove("testdata.txt")
# os.rmdir('new_directory')
# os.rmdir('parent')
# os.rename('old_name.txt','new_name.txt')
full_path = os.path.join('C:\\Users\\91771\\OneDrive - SmartCare Analytica AB\\Desktop\\Python Automtion\\Python Selenium\\pythonProject1\\src\\Sept\\ex_10_08_2024','file.txt')

print(full_path)

print(os.path.exists('file.txt'))

print(os.path.isfile('file.txt'))
print(os.path.isdir('directory_name'))