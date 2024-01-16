import Auto
def harmadik():
    kocsi = open("auto.txt", "r", encoding="utf-8")
    fejlec = kocsi.readline()
    beolvas = kocsi.readlines()
    kocsi.close()

def tabla():
    print("III/Tábla:")

def flotta():
    print("III/Flotta:")

def ertekes():
    print("III/Értékes")

def kiir():
    ki = open("kiir.txt", "a", encoding="utf-8")
    ki.close()
