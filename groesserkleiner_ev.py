def game(x):
    zahl_max = 100
    zahl_min = 1
    z = round((zahl_max - zahl_min)/2 + zahl_min, 0)
    counter = 1
    while x!=z:
        if z > x:
            zahl_max = z-1
        elif z < x:
            zahl_min = z+1
        z = round((zahl_max - zahl_min)/2 + zahl_min, 0)
        counter = counter + 1
    return counter

ev = 0
for x in range(100):
    ev = ev + game(x+1)
ev=ev/100
print(ev)


    


