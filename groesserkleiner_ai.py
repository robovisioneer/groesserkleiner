import random
x=random.randrange(1,100)
zahl_max = 100
zahl_min = 1
print("Waehlen Sie eine Zahl zwischen 1 und 100!")
print("Geben Sie 0 ein, um die Wahl der KI zu überlassen!")
y = input()
z=int(y)
if z == 0:
    z = round((zahl_max - zahl_min)/2 + zahl_min, 0)
    print("Zahl: ", z)
while x!=z:
    if z > x:
        print("Eingegebene Zahl zu hoch!")
        zahl_max = z-1
    elif z < x:
        print("Eingegebene Zahl zu niedrig!")
        zahl_min = z+1
    y = input()
    z=int(y)
    if z == 0:
        z = round((zahl_max - zahl_min)/2 + zahl_min, 0)
        print("Zahl: ", z)
else:
    print("Sie haben die richtige Zahl gefunden!")


    


