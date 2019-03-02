import random as r
import time as t

a = 1
win = [0, 1]
bal = 0

print("♥💰Lucky Lottery💰♥")

while a == 1:
    t.sleep(1)
    print("Starting game...")
    t.sleep(2)
    won = r.choice(win)
    if won == 1:
        print("You win $10!")
        bal = bal + 10
        print("Current balance: $", bal)
    if won == 0:
        print("You failed!")
        print("Current balance: $", bal)

    b = str(input("Want replay? ('yes' or 'no')"))
    if b == 'yes':
        if bal < 10:
            print("You haven`t enough money.")
            a = 0
        if bal >= 10:
            bal = bal - 10
            a = 1

print("Game ended.")
print("Goodbye!")

