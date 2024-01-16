import random

def Ottel_oszthato():
    szamok = []
    for szam in range(1, 51, 1):
        vszam = random.randint(1, 100)
        szamok.append(vszam)
    print("A lista elemei:")
    print(f"\t{szamok}")

    """
    oszto = 0
    if :
        oszto += 1
        print(f"A listában {oszto} darab öttel osztható szám van.")
    else:
        print("A listában nincs öttel osztható szám.")
    """