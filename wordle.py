from random import randrange

databaze_slov = ["běhat", "kopat", "viset", "létat", "kotel", "pasta", "boxer", "kapka", "slovo", "ježíš", "koláč", "pošta", "datel", "palec", "ježek", "kočka", "kráva", "fenka", "želva", "pokus", "sopka","kopec", "ovce", ] #databáze hledaných slov. Slova se mohou přidávat a mohou mít různý počet písmen bez dalších úprav programu.

vysledek = [] #proměnná typu seznam, sem budeme skládat průběžná vyhodnocení tiovaného slova
hledame_list = list(databaze_slov[randrange(len(databaze_slov))]) #náhodně vybere 1 slovo z "databaze_slov" a uloží do "hledame_list" jako seznam např. ["k", "o", "č", "k", "a"]
hledame_pomocna = [] #proměnná typu seznam
tip_list = [] #sem budeme ukládat tipované slovo a převedeme ho na seznam
#print("".join(hledame_list))

print("Hledáme slovo (podstatné jméno 1.pád č.j. nebo sloveso v infinitivu) na", len(hledame_list), "písmen. Máš 6 pokusů. Zadávej pouze malá písmena.")
print()
print(""" ABC - trefil jsi písmeno a pozici
 abc - trefil jsi písmeno, ale je na jiné pozici""")
print()

while len(tip_list) != len(hledame_list): #ověření, aby zadané/tipované slovo mělo práve 5 písmen
  tip_list = list(input("Tipni si: "))
  if len(tip_list) != len(hledame_list):
    print("Do", len(hledame_list), "snad umíš, ne?")

print()

for _ in range(5): #zajistí 5 pokusů - jeden již proběhnul, takže celkem 6 pokusů
  for i in range(len(tip_list)): #tady by mohlo být také jen (5), zkoumáme jednotlivá písmenka
    if hledame_list[i] == tip_list[i]: #porovná i-té písmeno hledaného slova a tipu
      hledame_pomocna.append(hledame_list[i].upper()) #vloží do "hledame_pomocna" i-té písmenko VELKÉ
    else:
      hledame_pomocna.append(hledame_list[i]) #pokud se i-té písmeno neshoduje s tipem, tak vloží do "hledame_pomocna" i-té písmeno, ale ne velké.
  #print(hledame_pomocna) #po tomto cyklu vypadá "hledame_pomocna" třeba takto ["k", "o", "Č", "k", "A"]

  for j in range(len(tip_list)): #poskládáme výsledek tipu
    if hledame_pomocna[j].isupper(): #pokud je j-té písmeno VELKÉ
      vysledek.append(hledame_list[j].upper()) #přidáme do proměnné "vysledek" j-té písmeno (VELKÉ)
    elif vysledek.count(tip_list[j]) < hledame_pomocna.count(tip_list[j]): #pokud je v seznamu "vysledek" ménší počet j-tého písmene než v seznamu "hledame_pomocna"
      vysledek.append(tip_list[j]) #přidá do proměnné "vysledek" j-té písmeno (malé)
    else:
      vysledek.append("_") #pokud není splněna žádná z výše uvedených podmínek, vloží do "vysledek" "_"
  
  print(" ".join(vysledek)) # vytiskne průběžný výsledek. (" ".join) slouží, aby vytištěný seznam vypadal takto "k _ Č _ A" a ne "k", "_", "Č", "_", "A"
  print()
   
  if hledame_list == tip_list: #tip se shoduje s hledaným slovem -> výhra
    break #ukončí cyklus
  
  tip_list.clear() #vyčistíme proměnnou
  
  while len(tip_list) != len(hledame_list): #načítáme další tip
    if 5 - _ == 5:
      print("Zbývá",5 -  _, "pokusů.") # tisk zbývajícího počtu pokusů
    elif 1 < 5 - _ < 5:
      print("Zbývají",5 -  _, "pokusy.")
    else:
      print("Máš poslední pokus")
    tip_list = list(input("Tipni si: "))
    if len(tip_list) != len(hledame_list):
      print("Do", len(hledame_list), "snad umíš, ne?")
    print()
    
  vysledek.clear() #vyčistíme proměnné a jdmeme na další pokus
  hledame_pomocna.clear()
      
print()
if hledame_list == tip_list: #výhra
  print("Gratuluji!!!")
else: #prohra
  print("Nevyšlo to. Slovo", "".join(hledame_list).upper(), "jsi neodhalil. Zkus to znovu.")
