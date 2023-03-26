import random

def navod(hledane_slovo):
  """Vytiskne návod"""
  print("Hledáme slovo (podstatné jméno 1.pád č.j. nebo sloveso v infinitivu) na", len(hledane_slovo), "písmen. Máš 6 pokusů.\n")
  print(""" ABC - trefil jsi písmeno a pozici
 abc - trefil jsi písmeno, ale je na jiné pozici\n""")
  

def databaze():
  """Náhodně vybere jedno slovo ze seznamu databaze_slov a vrátí ho"""
  databaze_slov = ["aroma", "běhat", "citrón", "gesto", "kopat", "viset", "létat", "kotel", "pasta", "boxer", "kapka", "slovo", "ježíš", "koláč", "pošta", "datel", "palec", "ježek", "kočka", "kráva", "fenka", "želva", "pokus", "sopka", "kopec", "ovce"] #databáze hledaných slov. Slova se mohou přidávat a mohou mít různý počet písmen bez dalších úprav programu.
  hledane_slovo = list(random.choice(databaze_slov)) #náhodně vybere 1 slovo z "databaze_slov" a uloží do "hledame_list" jako seznam např. ["k", "o", "č", "k", "a"]
  return hledane_slovo

def tip(hledane_slovo):
  """Vyzve uživatele k zadání tipovaného slova a tento tip převede na malá písmena a vrátí"""
  tip_list = []
  while len(tip_list) != len(hledane_slovo): #ověření, aby zadané/tipované slovo mělo práve 5 písmen
    tip_list = list(input("Tipni si: ").lower()) #zadaný vstup uloží do "tip_list" jako seznam a všechna písmena budou malá
    if len(tip_list) != len(hledane_slovo):
      print("Do", len(hledane_slovo), "snad umíš, ne?")
  return tip_list

def dalsi_hra(hrajeme_dal):
  """Ověří jestli uživatel odpověděl "ano" nebo "ne" a případně ho vyzve znovu. Pokud je odpověď "ano" vráni True, pokud "ne" vytiskne hlášku."""
  while hrajeme_dal not in ["ano", "Ano", "ANO", "ne", "NE", "Ne"]:
    print()
    print('Odpověz "ano" nebo "ne"')
    hrajeme_dal = input("Hrajeme dál? ano/ne \n")
      
  if hrajeme_dal in ["ano", "Ano", "ANO"]:
    return True
  else:
    print("\nTak zase příště.")
  