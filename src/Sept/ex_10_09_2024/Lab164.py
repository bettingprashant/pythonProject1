with open("Testdata.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="\n")
