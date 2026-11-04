print("Mysli si číslo od 1 do 100.")
print("Počítač se ho pokusí uhodnout.")
print("Odpovídej: v = větší, m = menší, s = správně.")

dole = 1 
nahore = 100
pokusy = 0 
odpoved = ""

while odpoved != "s":
    tip = (dole + nahore) // 2
    pokusy += 1

    print(f"Můj tip je: {tip}")
    odpoved = input("Je číslo větší (v), menší (m), nebo správně (s)? ")

    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
         nahore = tip - 1
    else:
        print("Uhodl jsem!")

print(f"Uhodl jsem tvoje číslo na {pokusy} pokusy!")