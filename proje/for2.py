def saydır():
 son = int(input("kaça kadar sayayım?"))

 ilk = int(input("kaçtan baslayayım"))

 artıs = int(input("kaçar kaçar artsın?"))
 say(son,ilk,artıs)
     
 for abc in range(son,ilk,artıs):
    print (abc,".sayı")

def say (x,y,z):
    for abc in range(x,y+1,z):
        print (abc)

