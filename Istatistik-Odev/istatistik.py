from os import system, path
# 20010011054 - ALİHAN DEMİRDAŞ

if path.exists("in.txt"):
    a = open("in.txt", 'r').read().splitlines()
    veri = []
    for x in a:
        veri.append(x)

else:
    print("Lütfen in.txt dosyası oluşturun ve yeniden çalıştırın. Şimdi program kapatılıyor.")
    input()
    exit()

# SINIF SAYISINI DOSYADAN ALIP, DAHA SONRA DOSYADAN SİLİYORUZ.
sinif_sayisi = int(veri[0])
del veri[0]
veri.sort()  # VERİYİ SIRALIYORUZ.
uzunluk = len(veri)  # TOPLAM KAÇ TANE VERİ VAR ONU BULUYORUZ.
alt_deger = float(min(veri))  # İLK ALT DEĞERİ BULUYORUZ.
ilk_alt = alt_deger
ust_deger = float(max(veri))  # ÜST DEĞERİ BULUYORUZ.
dagilim_genisligi = ust_deger - alt_deger
sinif_araligi = float((dagilim_genisligi+0.01) / sinif_sayisi)
sinif_araligi = round(sinif_araligi, 1)

toplamVeri = float()  # Ortalama için toplam
for x in veri:
    toplamVeri += float(x)

ortalama = toplamVeri / uzunluk


def mod(veri):  # MOD HESAPLAMA ALGORİTMASI
    listeler = {}
    for t in veri:
        if t in listeler:
            listeler[t] += 1
        else:
            listeler[t] = 1
    for t in listeler.keys():
        if listeler[t] == max(listeler.values()):
            return t


def frekansHesapla(a, b):  # FREKANS HESAPLAMA ALGORİTMASI
    toplam = int()
    for x in veri:
        if (float(x) > a or float(x) == a) and float(x) < b:
            toplam += 1
    return toplam


with open("out.txt", "a", encoding="utf-8") as dosya:  # DOSYAMIZI AÇIYORUZ
    liste = list()
    for a in range(sinif_sayisi):
        x = ilk_alt + (a*sinif_araligi) + (a*0.01)
        y = ilk_alt + sinif_araligi + (a*sinif_araligi) + (a*0.01)
        x = round(x, 2)
        y = round(y, 2)
        z = (x+y)/2
        z = round(z, 2)
        goreli = frekansHesapla(x, y)/uzunluk
        goreli = round(goreli, 2)
        liste.append(x)
        liste.append(y)
        liste.append(z)
        liste.append(frekansHesapla(x, y))
        liste.append(goreli)

    dosya.write("Alt    ")
    dosya.write("Üst    ")
    dosya.write("Orta   ")
    dosya.write("Frekans ")
    dosya.write("Göreli frekans")
    dosya.write("\n")

    for c in range(sinif_sayisi*5):
        if c % 5 == 0:
            if c == 0:
                pass
            else:
                dosya.write("\n")
        dosya.write(str(liste[c]))
        dosya.write("   ")

    dosya.write("\n\n")

    dosya.write("Ortalama       = ")
    dosya.write(str(ortalama))
    dosya.write("\n")

    dosya.write("Mod            = ")
    modd = str(mod(veri))
    dosya.write(modd[0:4])
    dosya.write("\n")

    dosya.write("Medyan         = ")
    orta = uzunluk // 2
    sonuc = (float(veri[orta]) + float(veri[~orta])) / 2
    dosya.write(str(sonuc))
    dosya.write("\n")

    dosya.write("Varyans        = ")
    sonucv = sum((float(i) - ortalama) ** 2 for i in veri) / uzunluk
    dosya.write(str(sonucv))
    dosya.write("\n")

    dosya.write("Standart Sapma = ")
    varyans = sum([((float(x) - ortalama) ** 2) for x in veri]) / uzunluk
    resultv = varyans ** float(0.5)
    dosya.write(str(resultv))
