#Create a list of 3 favorite fruits. Add a new fruit to the end, 
#then replace the second fruit with "Apple". Print the final list.

# 1. Başlangıç listesi
meyveler = ["Muz", "Çilek", "Karpuz"]

# 2. Sona yeni bir meyve ekleme
meyveler.append("Kivi")
print(meyveler)
# 3. İkinci meyveyi (index 1) "Apple" ile değiştirme
meyveler[1] = "Elma"

# 4. Final listeyi yazdırma
print(meyveler)
# Çıktı: ['Muz', 'Apple', 'Karpuz', 'Kivi']

meyveler2=["Erik","Dut","Nar"]
meyveler2.append("Armut")
print(meyveler2)
meyveler2[2]="Üzüm"
print(meyveler2)

#Create a list of 3 cities. Add a new city to the very end of the list and another city at the second position (index 1).

# 1. 3 şehirlik başlangıç listesi
sehirler = ["İstanbul", "Ankara", "İzmir"]

# 2. En sona yeni bir şehir ekleme
sehirler.append("Antalya")

print(f"Sona ekleme sonrası: {sehirler}")
# Çıktı: ['İstanbul', 'Ankara', 'İzmir', 'Antalya']

# 3. İkinci sıraya (index 1) "Bursa" ekleme
sehirler.insert(1, "Bursa")

# 4. Final listeyi yazdırma
print(f"Final listesi: {sehirler}")
# Çıktı: ['İstanbul', 'Bursa', 'Ankara', 'İzmir', 'Antalya']

sehirler2=["Sakarya","Rize","Van"]
sehirler2.append("Bolu")
sehirler2.insert(2, "Mugla")
print(sehirler2)
print(f"Final Listesi:{sehirler2}")

#Remove a city from the list by using its name. Then, remove the last remaining city in the list.

# Örnek listemiz
sehirler = ["İstanbul", "Bursa", "Ankara", "İzmir", "Antalya"]

# İsme göre "Ankara" şehrini silelim
sehirler.remove("Ankara")

print(f"İsme göre silme sonrası: {sehirler}")
# Çıktı: ['İstanbul', 'Bursa', 'İzmir', 'Antalya']

# Listenin en sonundaki şehri (Antalya) silelim
silinen_sehir = sehirler.pop()

print(f"Silinen son şehir: {silinen_sehir}")
print(f"Listenin son hali: {sehirler}")

sehirler3=["Sakarya", "Mus", "Artvin", "Afyon"]

sehirler3.remove("Mus")
print(sehirler3)
silinen_sehir2=sehirler3.pop()
print(silinen_sehir2)

#Create a list of unsorted numbers. Organize them so they are in descending order (from largest to smallest).

sayilar = [76, 92, 5, 18, 10, 99, 32]
sayılar2=[85,13,98,65,4,15]
# Listeyi kendi içinde büyükten küçüğe sırala
sayilar.sort(reverse=True)
print(sayilar)
sirali_yeni = sorted(sayılar2, reverse=True)
print(sirali_yeni)

#Find a way to count how many times a specific number appears in a list and identify the index position of that number.

sayilar = [10, 20, 30, 20, 40, 45, 50]
hedef = 20

# Hedef sayının kaç kez geçtiğini bul
tekrar_sayisi = sayilar.count(hedef)

print(f"{hedef} sayısı listede {tekrar_sayisi} kez geçiyor.")
# Çıktı: 20 sayısı listede 3 kez geçiyor.

sayılar4=[74,65,74,66,98,74,98]
hedef2=74

tekrar_sayisi2=sayılar4.count(hedef2)
print(tekrar_sayisi2)
print(f"{hedef2} sayısı listede {tekrar_sayisi2} kez geçiyor.")

# İlk görüldüğü yerin indeksi
ilk_konum = sayilar.index(hedef)

print(f"{hedef} sayısının ilk görüldüğü indeks: {ilk_konum}")
# Çıktı: 1 (Çünkü 20 ilk olarak 1. indekste)

ilk_konum2=sayılar4.index(hedef2)
print(f" {hedef2} satısının ilk görüldüğü indeks:{ilk_konum2}")

#Take a full list and remove every single item from it at once, leaving it completely empty.

meyveler = ["Elma", "Armut", "Muz", "Kivi"]

# Listeyi tamamen boşalt
meyveler.clear()

print(meyveler) 
# Çıktı: []

sayilar = [10, 20, 30, 40]

# Listenin tüm elemanlarını boşlukla değiştir
sayilar[:] = []

print(sayilar)
# Çıktı: []

