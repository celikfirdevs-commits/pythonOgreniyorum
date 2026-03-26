"""
Removing Items:
1. .pop() - İndeks ile Silme
Bir elemanı bulunduğu sıraya (indeksine) göre listeden çıkarmak için kullanılır.

Özellik: Eğer parantez içine bir sayı yazmazsanız, listenin en sonundaki elemanı siler.

Bonus: .pop() sildiği elemanı size geri verir. Yani sildiğiniz şeyi bir değişkene atayıp sonra kullanabilirsiniz.

oyuncular = ["Ali", "Veli", "Can"]
silinen = oyuncular.pop(1) # 1. indeksteki "Veli" silinir

print(oyuncular) # Çıktı: ['Ali', 'Can']
print(silinen)   # Çıktı: "Veli"

öğrenciler= ["firi","oguz","ırmak"]
print(öğrenciler)
silinen=öğrenciler.pop(0)
print(silinen)
print(öğrenciler)
"""
"""
2. .remove() - Değer ile Silme
Silmek istediğiniz elemanın yerini (indeksini) bilmiyorsanız ama adını (değerini) biliyorsanız bunu kullanırsınız.

Dikkat: Eğer listede aynı isimden iki tane varsa, .remove() sadece ilk bulduğunu siler.

sepet = ["Elma", "Muz", "Elma", "Çilek"]
sepet.remove("Elma") # Sadece ilk gördüğü "Elma"yı siler

print(sepet) # Çıktı: ['Muz', 'Elma', 'Çilek']

dolap=["elbise", "etek","kazak","elbise"]
dolap.remove("elbise")
print(dolap)   # Çıktı: ['etek', 'kazak', 'elbise']
"""
"""
3. .clear() - Her Şeyi Temizle
Listeyi tamamen boşaltmak istiyorsanız bunu kullanırsınız. Liste yok olmaz, ancak içindeki tüm elemanlar silinir ve elinizde boş bir liste [] kalır.

gorevler = ["Ders çalış", "Spor yap"]
gorevler.clear()

print(gorevler) # Çıktı: []

Kısa Özet: Hangisini Kullanmalıyım?
"3. sıradakini sil": .pop(2)

"En sondakini çıkar": .pop()

"Adı 'Muz' olanı sil": .remove("Muz")


"Her şeyi çöpe at": .clear()


Ordering: Listeleri belirli bir düzene sokmak, özellikle sayısal verilerle veya alfabetik isim listeleriyle çalışırken çok önemlidir. Python bu konuda bize iki temel araç sunar:
1 .sort() - Kalıcı Sıralama
Bu metot, listenin içeriğini küçükten büyüğe (sayılar için) veya alfabetik olarak (metinler için) kalıcı olarak sıralar.

Özellik: Orijinal listenin sırası değişir. Geri dönüşü yoktur (eski sırayı bir yere kaydetmediyseniz).

Ters Sıralama: Eğer büyükten küçüğe sıralamak isterseniz, parantez içine reverse=True yazabilirsiniz.

sayilar = [42, 10, 5, 100]
sayilar.sort()
print(sayilar) # Çıktı: [5, 10, 42, 100]

isimler = ["Zeynep", "Ali", "Can"]
isimler.sort()
print(isimler) # Çıktı: ['Ali', 'Can', 'Zeynep']

# Büyükten küçüğe sıralama
sayilar.sort(reverse=True)
print(sayilar) # Çıktı: [100, 42, 10, 5]
""" 
"""
sayılar= [87, 32, 58,69 ,5]
sayılar.sort()
print(sayılar)

isimler=["firi","lina","alin","pınar"]
isimler.sort()
print(isimler)
"""
