import not_belirleme
import sayıTahminetmeoyunu
import hesapmakinesi
def anaMenu():

  print("\033[1;36;40m")
  print(
    " ═════════════════════════╗") 
  print("║\033[1;36;40m ANA MENU ║")
  print("║                       ║")
  print("║1) Hesap Makinesi      ║")
  print("║2-) Sayı Tahmin etme   ║")
  print("║3-) Not belirleme      ║")
  print("║4-) ....               ║")  
  print("║   SEÇİMİNİZ NEDİR?    ║")
  print("║                       ║")
  print("╚═══════════════════════╩")
  secim = input()  
  print("Seçiniz:", secim)
  if secim == "3" :
    not_belirleme.gectikaldi()
  if secim == "1" :
    hesapmakinesi.hesapmakinesi()
  if secim == "2" :
    sayıTahminetmeoyunu.sayıtahminoyunu()
    

 


 
anaMenu()
