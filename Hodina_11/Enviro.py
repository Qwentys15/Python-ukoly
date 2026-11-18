import urllib.request

URL = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

odpoved = urllib.request.urlopen(URL)                   #otevření komunikace (uvedení objektu pro čtení pomocí https)

pocet_dni = 0
celkem_srazek = 0
radek = odpoved.readline()                                   #přečtení dat řádků

while bool(radek):
    text = radek.decode("utf-8").strip()
    srazka = float(text)
    if srazka>=0:
        celkem_srazek += srazka
        pocet_dni +=1
    radek = odpoved.readline()

odpoved.close()                           #uzavření komunikdace

print(f"Průměrné denní srážky: {celkem_srazek / pocet_dni}")