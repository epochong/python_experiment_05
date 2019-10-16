f = 13.0
i = 1
while (True):
    f = f * (1 + 0.008)
    if f > 26.0:
        break
    i += 1
print(i)