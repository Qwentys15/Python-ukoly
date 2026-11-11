#funkce pro výpočet obsahu obdelníka
def spocitej_obsah(a, b):
    #kontrola platnosti zadaných délek
    if a <= 0 or b <= 0:
        return None
    obsah = a * b
    return obsah 
#     return a * b

# ------ hlavní kod programu ------

print("VÝPOČET ROZLOHY BYTU")
pocet_mmistnosti = int(input("Zadej počet místností: "))
mistnost = 1
obsah = 0   # proměnná pro celkovou výměru bytu (součet dílčích obsahů)
while mistnost <= pocet_mmistnosti:
    print(f"Zadej rozměry {mistnost}. místnosti")
    a = int(input("Zadej rozměr \"a\":"))
    b = int(input("Zadej rozměr \"b\":"))
    obsah_mistnosti = spocitej_obsah(a, b)
    if obsah_mistnosti != None:
        obsah += obsah_mistnosti
        mistnost += 1 
print(f"Celková výměra byu je {obsah}")


