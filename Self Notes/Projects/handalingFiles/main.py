'''-------------------
Grady Glauser
Python File Handaling Project
May 22, 2024
-------------------'''

handalMode = input("What mode do you to go into \"read\", \"copy\", \"write\", \"edit\", or scan for duplicates aka \"scan\"?\n> ")

if handalMode == "read": #Read mode
    fileName = input("What file do you want to open?\n> ")
    file = open(fileName, "r+")
    for l in file.readlines():
        print(l, end="")
    file.close()

elif handalMode == "copy": #Copy mode
    fileName = input("What is the name of the file you want to copy?\n> ")
    newFileName = input("What is the name of the new file you want to create?\n> ")
    file = open(fileName, "r+")
    newFile = open(newFileName+".txt", "w")
    for line in file.readlines():
        newFile.write(file.readlines())

elif handalMode == "write": #write mode
    fileName = input("What is the name of the file you want to create?\n> ")
    file = open(fileName, "w")
    myLine = " "
    lineNum = 1
    while myLine != "":
        myLine = input("Line " + str(lineNum) + ":")
        file.write(myLine + "\n")
        lineNum += 1
    file.close()

elif handalMode == "edit": #edit mode
    fileName = input("What file do you want to edit?\n> ")
    lineNum = 1
    with open(fileName, "r") as file:
        fileLines = file.readlines()
        for l in fileLines:
            print(str(lineNum) + " " + l, end="")
            lineNum += 1
    with open(fileName, "r+") as file:
        editLineNumber = int(input("\nWhat line do you want to edit?\n> ")) - 1
        editLine = input("> ")
        fileLines[editLineNumber] = editLine + "\n"
        file.seek(0)
        file.writelines(fileLines)

elif handalMode == "scan": #scan mode
    
    fileNames = " "
    fileList = []
    fileDupes = []
    while fileNames != "":
        fileNames = input("What files do you want to scan for duplicates?\n> ")
        if fileNames != "":
            fileList.append(fileNames)

    
    for aName in fileList:
        with open(aName, "r") as fileA:

            contentA = fileA.readlines()
            for bName in fileList:
                if aName == bName:
                    continue
                with open(bName, "r") as fileB:
                    contentB = fileB.readlines()
                    
                    if contentA == contentB:
                        if aName not in fileDupes:
                            print(aName, bName, "y")
                            fileDupes.append(aName)
                            print(aName, bName, "z")
                        if bName not in fileDupes:
                            fileDupes.append(bName)

    print(fileDupes)

else:
    print("Invlid input")