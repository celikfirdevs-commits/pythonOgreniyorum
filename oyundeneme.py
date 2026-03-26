# ders 4
#örnek 1: 1-100 kadar asal sayıları ekrana yaz
#örnek 2:rasgele üretilen 10 sayıdan kaç tanesiasal bulan uygulama
#örnek 3: klavyeden girilem sayı asal mı değil mi kotrol eden uygulama
#örne 4: aynı örnekleri farklı tip sayılar içinde yapan uygulama (güzel sayı , mükemlle sayı,)

#kullanıcının aklından tuttuğu sayıyı 
#bilgisayarın tahmin etmesini sağlayan oyun kodlayın

import random

enKüçükDeğer=1
enBüyükDeğer=100
print("Aklından 1-100 arasında sayı tut")
denemesayısı=0
while True:
    print("{}-{}".format(enKüçükDeğer,enBüyükDeğer))
    bilgisayarınTahminEttiğiSayı=random.randint(enKüçükDeğer,enBüyükDeğer)
    cevap=input("{} tuttuğun sayı olabilir mi? [e]vet/ daha [b]üyük /daha[k]üçük:".format(bilgisayarınTahminEttiğiSayı))
    denemesayısı+=1
    if cevap=="e":
        print("Oley {} denemede Bildim".format(denemesayısı))
        break 
    elif cevap=="b":
        print("daha büyük denemeliyim")
        enKüçükDeğer=bilgisayarınTahminEttiğiSayı+1
    else:
        print("daha küçük denemeliyim")
        enBüyükDeğer=bilgisayarınTahminEttiğiSayı-1