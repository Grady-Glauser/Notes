'''-------------------
Grady Glauser
Python Reading Files
May 22, 2024
-------------------'''


file = open("readableFile.txt", "r+")
#r (read), w (write), a (append), r+ (read and write)
'''
print(file.readable())
print(file.readline())
print(file.readlines())

for line in file.readlines():
    print(line)

file.write("\nTest")
'''

newFileName = input("What is the name of the new file?\n> ")
newFile = open(newFileName+".txt", "w")
for line in file.readlines():
    newFile.write(line)


newFile.close()
file.close()