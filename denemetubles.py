"""
Demetler (Tuples), listelerin "değiştirilemez" kardeşleridir. Bir kez oluşturulduktan sonra içindeki verilerin değiştirilmesine izin vermezler. Bu özellikleri onları veritabanı kayıtları veya koordinatlar gibi "sabit" kalması gereken veriler için mükemmel kılar.

İşte Tuples yapısının temel özellikleri:
1. Tanımlama (Definition)
Demetler, listelerden farklı olarak normal parantez () kullanılarak oluşturulur.

Syntax: nokta = (10, 20)

Tek Elemanlı Tuple: Eğer sadece bir elemanlı bir demet oluşturacaksanız, 
Python'un bunun bir matematiksel parantez olmadığını anlaması için sonuna bir virgül 
koymalısınız:
tek_eleman = (5,)
2. Değiştirilemezlik (Immutability)
Demetlerin en büyük kuralı budur: Oluşturulduktan sonra değiştirilemezler.

Yeni eleman ekleyemezsiniz (.append() yoktur).

Var olan elemanı silemezsiniz (.pop() veya .remove() yoktur).

Bir indeksteki değeri güncelleyemezsiniz.

gunler = ("Pazartesi", "Salı", "Çarşamba")
gunler[0] = "Cuma" # <-- Bu kod HATA verir!

3. İndeksleme ve Dilimleme (Indexing & Slicing)
Tıpkı listelerde olduğu gibi, demetlerde de verilere indeks numaralarıyla ulaşırsınız. Sayma yine 0'dan başlar.

koordinat = (41.0082, 28.9784, "İstanbul")
print(koordinat[0])   # 41.0082
print(koordinat[:2])  # (41.0082, 28.9784)

4. Neden Liste Yerine Demet Kullanırız?
Eğer listeler daha esnekse, neden kısıtlayıcı olan Tuples kullanalım?

Güvenlik: Kodun ilerleyen kısımlarında önemli bir verinin (örneğin bir API anahtarı veya doğum tarihi) yanlışlıkla değiştirilmesini engeller.

Hız: Python, içeriği değişmeyeceğini bildiği için demetleri hafızada listelerden çok daha hızlı işler.

Sözlük Anahtarı: Demetler "değişmez" olduğu için Sözlüklerde (Dictionaries) anahtar olarak kullanılabilirler (Listeler kullanılamaz).

5. Tuple Paketi Açma (Unpacking)
Demetlerin en şık özelliklerinden biridir. Bir demetin içindeki değerleri tek seferde farklı değişkenlere atayabilirsiniz.

film = ("Inception", 2010, "Christopher Nolan")

isim, yil, yonetmen = film  # Paketi açtık

print(isim)     # Inception
print(yonetmen) # Christopher Nolan
Özetle: Verilerin değişmesini istiyorsan List, verilerin sabit kalmasını ve güvende olmasını istiyorsan Tuple kullanmalısın.
"""
"""
Sözlükler (Dictionaries), gerçek hayattaki sözlükler veya rehberler gibi çalışır. Bir kelimeye (Anahtar/Key) bakarsınız ve onun karşılığındaki tanımı (Değer/Value) bulursunuz.

Listelerden farkı, verilere 0, 1, 2 gibi sayılarla değil, kendi verdiğiniz anlamlı isimlerle ulaşmanızdır.
1. Tanımlama (Nasıl Oluşturulur?)
Sözlükler süslü parantez {} kullanılarak oluşturulur. Her veri çifti anahtar : değer şeklinde yazılır ve her çift arasına virgül , konur.

Syntax: sozluk = {"anahtar": "değer"}

Örnek:

kullanici = {
    "isim": "Can",
    "yas": 25,
    "sehir": "İstanbul"
}

kullanıcı={"isim":"firi, "yas":45, "sehir":"ankara"}
print("kullanıcı")

2. Temel Kurallar
Sözlükleri kullanırken unutmaman gereken iki altın kural vardır:

Anahtarlar (Keys) Benzersiz Olmalıdır: Bir sözlükte aynı isimde iki anahtar olamaz. Eğer aynı anahtarı tekrar kullanırsan, Python eski değerin üzerine yenisini yazar.

Anahtarlar Değiştirilemez (Immutable) Olmalıdır: Genellikle metin (string) veya sayı kullanılır. Listeler anahtar olamaz ama demetler (tuples) olabilir.

Değerler (Values) Her Şey Olabilir: Bir anahtarın karşısındaki değer; bir sayı, bir liste, hatta başka bir sözlük bile olabilir!

3. Neden Sözlük Kullanırız?
Bir arabanın özelliklerini bir listede tuttuğunu hayal et:
araba = ["Tesla", "Model 3", 2024, "Beyaz"]

Burada araba[2] dediğinde bunun "yıl" olduğunu ezbere bilmen gerekir. Ama bir Sözlük kullanırsan:

araba = {
    "marka": "Tesla",
    "model": "Model 3",
    "yil": 2024,
    "renk": "Beyaz"
}

print(araba["yil"]) # Çıktı: 2024 (Okuması ve anlaması çok daha kolay!)

motor={
    "marka":"yamaha",
    "model":"scooters",
    "yıl":2025,
    "renk":"mavi"
}
print(araba["yıl"])      BURDA NE PROBLEM VAR ????
"""