#example 1 - writing data in text file

# file=open("C:\Demofiles\myfile.txt.txt",'w')
# file.write("It is myfirst statement...\n")
# file.write("It is second statement...\n")
# file.write("It is third statement...\n")
# file.write("It is fourth statement...\n")
# file.write("It is fifth statement...\n")
# file.write("It is sixth statement...\n")
# file.close()
# print("Program completed")

#Example 2 Reading data in text file

# file=open("C:\Demofiles\myfile.txt.txt",'r')
# print(file.readline())
# file.close()

#Example 3 appending data into text file

file=open("C:\Demofiles\myfile.txt.txt",''
                                        'a')
file.write("\n It is seventh statement...\n")
file.write("It is eighth statement...\n")

file.close()
print("program completed")