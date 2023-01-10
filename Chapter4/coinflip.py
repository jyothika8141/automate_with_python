import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    lst = []
    for i in range(100):
        lst.append(random.randint(0, 1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(94):
        if lst[j:j+6] == [0,0,0,0,0,0] or lst[j:j+6] == [1,1,1,1,1,1]:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
