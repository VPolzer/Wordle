from vstupy import navod, databaze, tip, dalsi_hra
from porovnani import porovnej, poskladej 
from vyhodnoceni import vyhodnot, pokusu, nepotrebna

def main():
  zobrazit_navod = True
  while True:
    hledane_slovo = databaze() #vybere náhodné slovo z databáze slov a uloží do proměnné
    print(hledane_slovo)
    nepotrebna_pismena = [] #proměnná typu seznam
    if zobrazit_navod: # aby se návod tiskunl jen v prvím kole hry 
      navod(hledane_slovo) #vytiskne návod
      zobrazit_navod = False
    else:
      print("\nHledáme slovo na", len(hledane_slovo), "písmen.\n")
    
    for k in range(6): #máme 6 pokusů
      tip_list = tip(hledane_slovo) #vyzve uživatele k zadání slova a uloží do proměnné
      print()
      hledame_pomocna = porovnej(hledane_slovo, tip_list) #porovná tip a hledané slovo a výsledek uloží do proměnné
      print(" ".join(poskladej(tip_list, hledame_pomocna, hledane_slovo))) # vytiskne průběžný výsledek. (" ".join) slouží, aby vytištěný seznam vypadal takto "k _ Č _ A" a ne "k", "_", "Č", "_", "A"
      if hledane_slovo != tip_list: #tip se neshoduje s hledaným slovem
        nepotrebna(hledane_slovo, tip_list, nepotrebna_pismena) #vytiskne nepotřebná písmena
        pokusu(k, tip_list) #vytiskne počet pokusů 
      print()
      if hledane_slovo == tip_list: #tip se shoduje s hledaným slovem -> výhra
        break #ukončí cyklus
     
    vyhodnot(hledane_slovo, tip_list) #vyhodnotí jestli uživatel uhodnul a vytiskne příslušnou hlášku 
    
    hrajeme_dal = input("Hrajeme dál? ano/ne \n")
    if not dalsi_hra(hrajeme_dal):
      break
         
main()