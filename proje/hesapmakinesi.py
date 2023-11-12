def hesapmakinesi():


  print("\033[1;36;40m")
  print(" ╔══════════════════╗") 
  print("║\033[1;36;40m HESAP MAKİNESİ║")
  print("║                       ║")
  print("║1-) TOPLAMA            ║")
  print("║2-) ÇIKARMA            ║")
  print("║3-) ÇARPMA             ║")
  print("║4-) BÖLME              ║")
  print("║                       ║")
  print("╚═══════════════════════╩")
  secim = input()  
  print("Seçiniz:", secim)
  if secim == "1" :toplama()

  print ("TOPLAMAYI SECTİNİZ") 
  sayi1 = int(input("1. SAYIYI GİRİNİZ:")) 
  sayi2 = int(input("2. SAYIYI GİRİNİZ:"))  
  print("SAYILAR TOPLAMI:", sayi1 + sayi2) 


