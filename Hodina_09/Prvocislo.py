
import math

print("JE ZADANÉ ČÍSLO PRVOČÍSLEM?\n")
cislo = int(input("Zadej celé číslo: "))

je_prvocislem = True            #stavová proměnná

if cislo<2 :
    je_prvocislem = False
elif cislo == 2:
    je_prvocislem = True
elif cislo % 2 == 0:
    je_prvocislem = False
else:
    delitel = 3
    while delitel<math.sqrt(cislo):
        if cislo % delitel == 0:
            je_prvocislem = False
            break
        delitel += 2

if je_prvocislem:
    print(f"Číslo {cislo} JE prvočíslo. ")
else:
    print(f"Číslo{cislo} NENÍ prvočíslo. ")
