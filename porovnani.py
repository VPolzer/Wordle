def porovnej(hledane_slovo, tip_list):
  """Načte hledané slovo a tipované slovo, porovná je a vrátí tipované slovo, ve kterém jsou velkým písmem vyznačena písmena, která se shodují (písmeno i pozice) s hledaným slovem (např. k o Č k A)""" 
  hledame_pomocna = []
  for i in range(len(hledane_slovo)): #tady by mohlo být také jen (5), zkoumáme jednotlivá písmenka
      if hledane_slovo[i] == tip_list[i]: #porovná i-té písmeno hledaného slova a tipu
        hledame_pomocna.append(hledane_slovo[i].upper()) #vloží do "hledame_pomocna" i-té písmenko VELKÉ
      else:
        hledame_pomocna.append(hledane_slovo[i]) #pokud se i-té písmeno neshoduje s tipem, tak vloží do "hledame_pomocna" i-té písmeno, ale ne velké.
  #print(hledame_pomocna) #po tomto cyklu vypadá "hledame_pomocna" třeba takto ["k", "o", "Č", "k", "A"]
  return hledame_pomocna

def poskladej(tip_list, hledame_pomocna, hledane_slovo):
  """Poskládá slovo, ve ktekém jsou vyznačena velkými písmeny písmena, která jsou na správné pozici, malými písmeny písmena, která jsou ve hledaném slově, ale na jiné pozici a "_" pokud dané písmeno v hledaném slově není (např. K _ Č _ a)"""
  vysledek = []
  for j in range(len(hledame_pomocna)): #poskládáme výsledek tipu
    if hledame_pomocna[j].isupper(): #pokud je j-té písmeno VELKÉ
      vysledek.append(hledane_slovo[j].upper()) #přidáme do proměnné "vysledek" j-té písmeno (VELKÉ)
    elif vysledek.count(tip_list[j]) < hledame_pomocna.count(tip_list[j]): #pokud je v seznamu "vysledek" ménší počet j-tého písmene než v seznamu "hledame_pomocna"
      vysledek.append(tip_list[j]) #přidá do proměnné "vysledek" j-té písmeno (malé)
    else:
      vysledek.append("_") #pokud není splněna žádná z výše uvedených podmínek, vloží do "vysledek" "_"
  return vysledek 