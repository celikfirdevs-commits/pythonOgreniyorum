#ders 2
#pythonda karar yapıları -if
# == eşitse
# < küçükse
# > büyükse
# <= küçük veya eşitse
# >= büyük veya eşitse
# != eşit değilse

"""
yas=28
if yas>18:
    print("18 yaşından büyüksünüz")
    input("sınava bağvurmak istiyor musun?")
    ortalama=int(50+60)/2
    print(ortalama)
elif yas==18:
    print("18 yaşındasınız")
else:
    print("18 yaşından küçüksünüz")
"""
"""
isim=input("Öğrencinin adını giriniz:")
not1=input("1. notunu giriniz:")
not2=input("2. notunu giriniz:")

ortalama=(int(not1)+int(not2))/2

print(ortalama)

if ortalama>=70:
    print("geçtiniz")
else:
    print("kaldınız")
"""
# and
# 1 and 1=1
# 1 and 0=0
# 0 and 1=0
# 0 and 0=0

#or
# 1 or 1=1
# 1 or 0=1
# 0 or 1=1
# 0 or 0=0

"""
kullanıcıadı=input("Kullanıcı adını giriniz:")
şifre=input("şifrenizi giriniz:")

if kullanıcıadı=="firdevs" and şifre=="1234":
    print("Giriş Başarılı")
else:
    print("kullanıcı adı veya şifre hatalı")
"""

kullanıcıadı=input("Kullanıcı adını giriniz:")
#şifre=input("şifrenizi giriniz:")

if kullanıcıadı=="firdevs":
    şifre=input("şifrenizi giriniz:")
    if şifre=="1234":
        print("giriş başarılı")
    else:
        print("şifre hatalı)")
else:
    print("kullanıcı adını hatalı")
