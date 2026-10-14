# kontrola, zada bod leží v zadané oblasti nebo mimo ní
xb = int(input("Zadej X Souřadnici bodu : "))
yb = int(input("Zadej Y Souřadnici bodu : "))

x1_oblast = 5 
y1_oblast = 2 
x2_oblast = 10
y2_oblast = 7

if xb>=x1_oblast and xb<x2_oblast and yb>=y1_oblast and yb<y2_oblast:
   print("Bod leží uvnitř oblasti")
else:
   print("Bod leží mimo oblas")

#Bod leží na hranici

lezi_na_1 = xb>=x1_oblast and xb<=x2_oblast and yb==y1_oblast
lezi_na_2 = yb>=y1_oblast and yb<=y2_oblast and xb==x2_oblast
lezi_na_3 = xb>=x1_oblast and xb<=x2_oblast and yb==y2_oblast
lezi_na_4 = yb>=y1_oblast and yb<=y2_oblast and xb==x1_oblast

   
if lezi_na_1 or lezi_na_2 or lezi_na_3 or lezi_na_4:
   print("Bod leží na hranici oblasti")
else:
   print("Bod leží mimo hranici oblasti")