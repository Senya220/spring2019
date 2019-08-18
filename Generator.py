import time

outpt = open('Output.txt', 'a')
inpt = str(input("Input your text here: "))
a = 0
b = 0
lst = []

outpt.write("[ ")

for i in range(len(inpt)):
    lst.append(inpt[a])
    a = a + 1

b = len(lst)
for i in range(len(lst)):
    outpt.write(lst[b - 1])

    b = b - 1
    time.sleep(0.2)
    print("Process is running...")

outpt.write(" ] ")
outpt.close()
print("Process finished")
