cas = float(input("Zadej čas: ")) 

if cas<0:
    print("Chybné zadán!")
elif cas<5:
    print("Dobrou noc")
elif cas<10:
    print("Dobré ráno")
elif cas<12:
    print("Dobré dopoledne")
elif cas<19:
    print("Dobré odpoledne")
elif cas<21:
    print("Dobrý večer")