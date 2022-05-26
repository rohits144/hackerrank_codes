a = 1000
pl = list(range(a+1))
for i in range(a+1):
    for j in range(2, int(i/2)+1):
        if i%j == 0:
            pl.remove(i)
            break


print(pl)