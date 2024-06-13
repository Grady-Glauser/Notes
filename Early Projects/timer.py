import time

timer = 1

print("How long: ")

setTime = input()

while int(timer) <= int(setTime):
    print("----")
    print("-" + str(timer) + "-")
    print("----")
    time.sleep(1)
    timer = int(timer) + 1
print("----------")
print("-Times Up-")
print("----------")