import random
x=random.randrange(1,100)
print("Waehlen sie eine Zahl zwischen 1 und 100")
y = input()
z=int(y)
while x!=z:
    if z > x:
        print("Eingegebene Zahl zu hoch!")
    elif z < x:
        print("Eingegebene Zahl zu niedrig!")
    y = input()
    z=int(y)
else:
    print("Sie haben die richtige Zahl gefunden!")


    


