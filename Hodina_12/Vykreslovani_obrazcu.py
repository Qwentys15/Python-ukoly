# Vykreslování obrazc§ hvězdiček

print("VÍTEJ V PROGRAMU PRO KRESLENÍ GEOMETRICKÝCH TVARŮ")

def ctverec(strana):
    i = int(input("Délka strany?"))
    radek = 0
    while radek < strana:
        print("*" * strana)
        radek += 1

def ctverec_duty(strana):
    i = int(input("Délka strany?"))
    radek = 0
    while radek < strana:
        if radek == 0 or radek == strana - 1:
            print("*" * strana)
        else:
            print("*" + " " * (strana - 2) + "*" )
        radek += 1

def obdelnik(strana):
    a = int(input("Délka strany a? "))
    b = int(input("Délka strany b? "))
    radek = 0
    while radek < b:
        print("*" * a)
        radek += 1

pokracovat = True
while pokracovat:
    volba = input("Jaký obrazec chceš vykreslit? [c, cn, ob]")
    if volba == "c":
        ctverec()
    elif volba == "cn":
        ctverec_duty()
    elif volba == "ob":
        obdelnik()
    else:
        print("Neplatný výběr! Vyber z [c, cn]")
    odpoved = input("Chceš vykreslit další obrazec? [ano / ne]")
    if odpoved != "ano":
        pokracovat = False
print("DĚKUJI ZA POUŽITÍ PROGRAMU")