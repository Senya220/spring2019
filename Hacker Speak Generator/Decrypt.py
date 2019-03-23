import time

outpt = open('Output.txt', 'a')
inpt = str(input("Input encrypted text here (If you input numbers, they may be decrypted!!!): "))
a = 0
b = 0
lst = []

outpt.write(" [ ")

for i in range(len(inpt)):
    lst.append(inpt[a])
    a = a + 1

for i in range(len(lst)):
    if lst[b] == '4':
        outpt.write("a")
    else:
        if lst[b] == '3':
            outpt.write("e")
        else:
            if lst[b] == '0':
                outpt.write("o")
            else:
                if lst[b] == '1':
                    outpt.write("i")
                else:
                    outpt.write(lst[b])
    b = b+1
    time.sleep(0.2)
    print("Process is running...")

outpt.write(" ]")
outpt.close()
print("Process finished")
