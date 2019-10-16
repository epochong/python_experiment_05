i = 1
while (True):
    if i % 2 == 1 and i % 3 == 2 and i % 4 == 3 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
        break
    i += 1
print(i)