import os
try:
    file = open('testd ata.txt','r')
    print(file.read())
except FileNotFoundError as fnf:
    print("File not found check the path")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)