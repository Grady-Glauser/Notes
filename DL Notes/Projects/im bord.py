#List setup
listOne = [1,1,2,3,3,3,4,5,5]
listTwo = [1,2,3,4,5]
listThree = []

for i in listOne: #Loops throught first list
    if i not in listThree: #Cheks to see if number is not allready on the finle list
        listThree.append(i) #If the number is not allready oin the list it will be added or appended

for n in listTwo:
    if n not in listThree:
        listThree.append(n)

listThree.sort() #Just to make it fancy

print(listThree) #You got to print it, duh




arr = [1,2,3,4,5]
answer = 1
def multiplyArray(arr,answer):
    for x in arr:
        answer = answer*int(x)
    print(answer)
multiplyArray(arr,answer)



zeroList = [1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,1,1]
zeroInLoop= 0
zeroTotalCount = 0
isZero = False
for z in zeroList:
    if z == 0:
        isZero = True
    else:
        isZero = False
    if isZero == True:
        zeroInLoop = zeroInLoop + 1
    else:
        zeroInLoop = 0
    if zeroInLoop > zeroTotalCount:
        zeroTotalCount = zeroInLoop
print(zeroTotalCount)


