def gectikaldi():
    puan = int(input ("notu giriniz: "))
    if puan < 50 :
        print (" gecemedin ")
    if puan > 50 :
        print (" aferin gectin")
        
    else:
        if  puan > 90 : print ("mükemmelsin")
        elif puan > 70: print ("fena degil")
        elif puan > 60: print (" biraz daha calismalisin")
    if puan > 100 or  0 :print(" 0 ile 100 arasi bi sayı girebilirsin")
