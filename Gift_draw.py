import random

cekilise_katilanlar=["Fatma", "Aysenur", "Zuhal", "Damla","Ilayda", "Hanife","Begüm", "Baris", "Yakup", "İbrahim", "Vedat", "Zeynep","Aybike","Hasan"]

def hediye_cekilisi():
    alan_kisi= cekilise_katilanlar.copy()
    veren_kisi= cekilise_katilanlar.copy()
    
    while len(alan_kisi)>0:

         alan_kisi_index= random.randint(0, len(alan_kisi)-1)
         veren_kisi_index= random.randint(0, len(veren_kisi)-1)

         while alan_kisi[alan_kisi_index]== veren_kisi[veren_kisi_index]:
            alan_kisi_index= random.randint(0, len(alan_kisi)-1)
            veren_kisi_index= random.randint(0, len(veren_kisi)-1)


         print(alan_kisi[alan_kisi_index], "Şu kişiye hediye alacak:", veren_kisi[ veren_kisi_index])
         del alan_kisi[alan_kisi_index]
          # del cekilise_katilanlar[veren_kisi_index]
         veren_kisi.remove(veren_kisi[veren_kisi_index])    
    

hediye_cekilisi()