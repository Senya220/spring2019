import time

outpt = open('Output.txt', 'a')
inpt = str(input("Input your text here (Special symbols and capital letters are not encrypted!!!): "))
a = 0
b = 0
lst = []

outpt.write(" [ ")

for i in range(len(inpt)):
    lst.append(inpt[a])
    a = a + 1

for i in range(len(lst)):
    if lst[b] == 'a':
        outpt.write("4")
    else:
        if lst[b] == 'e':
            outpt.write("3")
        else:
            if lst[b] == 'o':
                outpt.write("0")
            else:
                if lst[b] == 'i':
                    outpt.write("1")
                else:
                    outpt.write(lst[b])
    b = b+1
    time.sleep(0.2)
    print("Process is running...")

outpt.write(" ]")
outpt.close()
print("Process finished")
