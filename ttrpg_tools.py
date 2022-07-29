import random
rollList = []
rollDieList = []
die = [4,6,8,10,12,20]
def roll(d = 20):
    rollList.append(random.randint(1, d+1))
    rollDieList.append(d)
for i in range(100):
    roll(die[random.randint(0,5)])
    print("{:<5} {:<50}{:<50}".format(str(i),str(rollList), str(rollDieList)))
    if i%12 == 0:
        if i != 0:
            rollList.clear()
            rollDieList.clear()
