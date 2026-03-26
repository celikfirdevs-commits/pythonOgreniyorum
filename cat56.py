"""
#Tanımlama (Definition)
#Listeler köşeli parantez [] kullanılarak oluşturulur. İçerisinde her türlü veri tipini 
#(yazı, sayı, hatta başka bir listeyi) barındırabilir.
"""
"""
meyveler = ["Elma", "Muz", "Çilek"]
karisik = [10, "Merhaba", True, 3.14]

print(meyveler)
print(karisik)
"""
"""
#Değiştirilebilirlik (Mutability)
#yani liste oluşturulduktan sonra elemanlarını tek tek 
#güncelleyebilirsin.

programlar = ["Python", "Java", "C++"]
programlar[1] = "C#"  # Java yerine C# geldi
print(programlar)     # Sonuç: ['Python', 'C#', 'C++']

netlik=[ "ayşe", "fatma", "hasan"]
netlik[0]="firi"
print(netlik)
"""
"""
#İndeksleme ve Dilimleme (Indexing & Slicing)
#Python'da sayma her zaman 0'dan başlar.

#İndeks: Tek bir elemana ulaşmak.

#Dilimleme: Belirli bir aralığı almak 
#[başlangıç : bitiş]. (Bitiş indeksi dahil edilmez).

sayilar = [10, 20, 30, 40, 50]
print(sayilar[0])      # 10 (İlk eleman)
print(sayilar[1:4])    # [20, 30, 40] 
#(1. indexten başla, 4. indexe kadar git ama 4'ü alma)

sayılar1=[ 5,10,15,20,25]
print(sayılar1[1])
print(sayılar1[0:3])
"""