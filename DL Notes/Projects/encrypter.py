letters = ["a","b","c","d","e","f","g","h","i",'j',"k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

message = input("Your message: ").lower()
encrypiterNumber = int(input("Encription seed: "))*2
messageList = []

for m in message:
    messageList.append(m)

for l in messageList:
    if l in letters:
        if encrypiterNumber%2 == 0:
            encrypiterNumber = letters.index(l)+12
        else:
            encrypiterNumber = letters.index(l)-12

        while encrypiterNumber > 25:
            encrypiterNumber =- 25
    
    if