import random as r
import time as t

a = 1
win = [0, 1]
bal = 0

print("♥💰Lucky Lottery💰♥")
print("")

while a == 1:
    t.sleep(1)
    print("Starting game...")
    print("")
    t.sleep(2)
    won = r.choice(win)
    if won == 1:
        print("You win $15!")
        bal = bal + 15

    if won == 0:
        print("You failed!")

    print("Current balance: $", bal)
    print("")

    if bal < 10:
        print("You haven`t enough money to replay.")
        print("")
        a = 0
    if bal >= 10:
        print("Payed $10 successfully. Be ready to next round! ")
        print("")
        bal = bal - 10
        a = 1

print("Game ended.")
print("Goodbye!")
