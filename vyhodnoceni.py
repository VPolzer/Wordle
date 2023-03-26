def vyhodnot(hledane_slovo, tip_list):
  """Vyhodnotí, zda se shoduje hledané slovo a tipované slovo a vytiskne příslušnou hlášku"""
  if hledane_slovo == tip_list: #výhra
    print("Gratuluji!!!\n")
  else: #prohra
    print("Nevyšlo to. Slovo", "".join(hledane_slovo).upper(), "jsi neodhalil. Zkus to znovu.\n")
  

def pokusu(k, tip_list):
  """Vytiskne zbývající počet pokusů"""
  if 5 - k == 5:
    print("Zbývá",5 - k, "pokusů.") # tisk zbývajícího počtu pokusů
  elif 1 < 5 - k < 5:
    print("Zbývají",5 - k, "pokusy.")
  elif k == 4:
    print("Máš poslední pokus.")

def nepotrebna(hledane_slovo, tip_list, nepotrebna_pismena):
  """Tiskne a vrací písmena, která byla v tipu, ale nejsou ve hledaném slově"""
  for i in tip_list:
    if i not in hledane_slovo and i not in nepotrebna_pismena:
      nepotrebna_pismena.append(i) #vloží písmeno
      nepotrebna_pismena.sort() # seřadí nepotřebná písmena abecedně
  print("Nepotřebná písmena: ", end="") 
  print(", ".join(nepotrebna_pismena)) #vytiskne nepotrebna_pismena a oddělí čárkou
  print()
  return nepotrebna_pismena