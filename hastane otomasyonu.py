
def baslik():
    print("############################################")
    print("#         HASTA KAYIT SİSTEMİ              #")
    print("############################################")

def secimYap():
    return int(input("Hasta Kayıt Sistemine Hoşgeldiniz!!\nMenüden seciminizi yapınız:(1 ve 12 arasında secim yapınız.1 ve 12 dahil) \nSeciminiz:"))

def menu():
    print("\n\n***************MENU*********************")
    print("*1.Hasta Görüntüleme                     *")
    print("*2.Hasta Güncelleme                      *")
    print("*3.Hasta Arama                           *")
    print("*4.Hasta Silme                           *")
    print("*5.Hasta Yatış Süresi                    *")
    print("*6.Hasta Ekleme                          *")
    print("*7.Hasta Bilgilerini Dosyaya Yaz         *")
    print("*8.Hasta Bilgilerini Dosyadan Okuma      *")
    print("*9.Hasta Yatış Masrafları                *")
    print("*10.Korona Testi                         *")
    print("*11.Hasta Refakatçi Sayısı Belirleme     *")
    print("*12.Sistemden Çıkış                      *")
    print("******************************************")


hasta_dict = {
    0: {
        "Hasta Adı Soyadı" :"Mehmet Arıktekin",
        "Hasta Telefon": "05057689434",
        "Hastanın Durumu" : "kötü",
        "Yatış Masrafı" : 450,
        "Korona Sonuç" : 'pozitif',
        "Refakatci Sayısı": 0,
        "Yatış Gün Sayısı":18
    },
    1: {
        "Hasta Adı Soyadı" :"Müzeyyen Kara",
        "Hasta Telefon": "05423212323",
        "Hastanın Durumu" : "iyi",
        "Yatış Masrafı" : 100,
        "Korona Sonuç" : 'negatif',
        "Refakatci Sayısı": 0,
        "Yatış Gün Sayısı": 1
    },
    2: {
        "Hasta Adı Soyadı" :"Leyla Kaya",
        "Hasta Telefon": "0504563213",
        "Hastanın Durumu" : "kötü",
        "Yatış Masrafı" : 400,
        "Korona Sonuç" : 'pozitif',
        "Refakatci Sayısı": 0,
        "Yatış Gün Sayısı": 35
    },
    3: {
        "Hasta Adı Soyadı" :"Şaziye Kara",
        "Hasta Telefon": "05423212323",
        "Hastanın Durumu" : "iyi",
        "Yatış Masrafı" : 100,
        "Korona Sonuç" : 'negatif',
        "Refakatci Sayısı": 0,
        "Yatış Gün Sayısı": 5
    }

}
def hasta_goruntuleme(hasta_dict):
    for h_id, h_info in hasta_dict.items():
        print("\nHasta No:", h_id)

        for key in h_info:
            print(key + ':', h_info[key])
    menuden_cikis()


def  hasta_bilgilerini_dosyadan_oku():
    print("Dosyadaki kayıtlı hastalarımız\n")
    oku = open("14010011015.txt")
    print(oku.read())
    oku.close()
    menuden_cikis()

def hasta_guncelleme(hasta_dict):
    # sözlükteki tüm degerler
    print("Tüm Hastalar\n")
    for item in hasta_dict:
      print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))
   # hasta_bilgilerini_dosyadan_oku()
    print("\n\n")
    id = int(input("Güncellenecek Hasta No'sunu tamsayı şeklinde giriniz:"))

    if (id in hasta_dict):
        guncelleme_secim = int(input("Hasta AdıSoyadı Güncellemek için 1,\n"
              "Hasta Telefonunu Güncellemek için 2,\n"
              "Hasta Durumunu Güncellemek için 3,\n"
              "Hasta yatış masraflarını güncellemek 4,\n"
              "Hasta korona sonucunu güncellemek için 5,\n"
              "Hastanın refakatci sayısını güncellemek iciç 6 seçimini yapınız:"))

        if(guncelleme_secim == 1):

           ad = str(input("Güncellenecek Hastanın Adını ve Soyadını giriniz:"))
           d1 = {"Hasta Adı Soyadı": ad}
           hasta_dict[id].update(d1)
           print(d1)
           hasta_bilgilerini_dosyaya_yaz(hasta_dict)
        elif (guncelleme_secim == 2):

            tel = str(input("Güncellenecek Hastanın telefonunu giriniz:"))
            d2 = {"Hasta Telefon": tel}
            hasta_dict[id].update(d2)
            print(d2)
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)

        elif (guncelleme_secim == 3):

            durum = str(input("Güncellenecek Hastanın durumunu iyi yada kötü olarak giriniz:"))
            d3 = {"Hastanın Durumu": durum}
            hasta_dict[id].update(d3)
            print(d3)
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)

        elif (guncelleme_secim == 4):

            yatis_masrafi = int(input("Güncellenecek Hastanın yatış masrafını giriniz:"))
            d3 = {"Yatış Masrafı": yatis_masrafi}
            hasta_dict[id].update(d3)
            print(d3)
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)

        elif (guncelleme_secim == 5):

            korona_sonu = str(input("Güncellenecek Hastanın korona sonucunu (pozitif/negatif şeklinde) giriniz:"))
            d3 = {"Korona Sonuç": korona_sonu}
            hasta_dict[id].update(d3)
            print(d3)
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)

        elif (guncelleme_secim == 6):

            refakatci = int(input("Güncellenecek Hastanın refaktci sayısını  tam sayı olarak giriniz:"))
            d3 = {"Refakatci Sayısı": refakatci}
            hasta_dict[id].update(d3)
            print(d3)
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)
        else:
            print("Gecerli bir güncelleme değeri secin")

    else:
        print("Güncellenecek hastanın no'su hasta sözlüğümüzde bulunmamaktadır!\n\n")
        return False

    menuden_cikis()

def hasta_arama(hasta_dict):
    print("Aramak istediğiniz Hasta No'sunu giriniz..")

    id = int(input("Hasta No'sunu giriniz:(Tam sayı değerleri giriniz.)"))

    if (id in hasta_dict):
        print("Aranılan Hasta No'su hasta sözlüğümüzde bulunmaktadır.\n")
        menuden_cikis()
    else:
        print("Aranılan Hasta No'su sözlüğümüzde bulunmamaktadır!")
        return False

def hasta_silme(hasta_dict):
    # sözlükteki tüm degerler
    for item in hasta_dict:
        print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))

    id = int(input("Yukarıdaki listeden bakıp Silmek istediğiniz Hasta No'sunu giriniz:"))

    if(id in hasta_dict):
        del hasta_dict[id]

        print("Yeni liste")

        for item in hasta_dict:
            print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))
    else:
        print("Böyle bir hasta nosu bulunmamaktadır.")
    menuden_cikis()

def hasta_yatis_suresi(hasta_dict):
    # sözlükteki tüm degerler
    print("Tüm Hastalar\n")
    for item in hasta_dict:
        print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))

    print("Yatis suresini ogrenmek istediğiniz Hasta No'sunu giriniz..")

    id = int(input("(Tam sayı değerleri giriniz.)"))

    if (id in hasta_dict):
        if(hasta_dict[id]["Hastanın Durumu"] == "kötü"):
            print("Hastanın yatış süresi bir aydan fazladır.")

        elif(hasta_dict[id]["Hastanın Durumu"] == 'orta'):
            print("Hastanın yatış süresi 1 hafta ile 4 hafta arasındadır.")

        else:
            print("hastanın yatış suresi bir haftadan azdır. Çünkü hastanın durumu iyidir")
    else:
        print("Böyle bir hasta numarası sözlüğümüzde bulunmamaktadır.")

    menuden_cikis()
def hasta_ekleme(hasta_dict):

    print("Yeni Hasta Eklemek için doldurmanız gereken bilgiler:")

    id = int(input("Hasta No'sunu giriniz:"))

    if (id in hasta_dict):
        print("Girdiğiniz Hasta No'su zaten sözlüğümüzde bulunmaktadır!Başka bir Hasta No'su giriniz..")
        hasta_ekleme(hasta_dict)
    else:
        hasta_dict[id] = {}
        hasta_dict[id]['Hasta Adı Soyadı'] = str(input("hastanın Adını Soyadını giriniz:"))
        hasta_dict[id]['Hasta Telefon'] = int(input("hastanın telefon bilgilerini giriniz:"))
        hasta_dict[id]['Hastanın Durumu'] = str(input("hastanın durumunu giriniz:"))
        hasta_dict[id]["Yatış Masrafı"] = int(input("hastanın yatış masrafını giriniz:"))
        hasta_dict[id]["Korona Sonuç"] = str(input("hastanın korona sonucunu giriniz:(Pozitif/negatif)"))
        hasta_dict[id]["Refakatci Sayısı"] = int(input("hastanın refakatci sayısını giriniz:"))

        # hasta yeni eklenen deger
        print("Yeni Eklenen hasta Bilgileri:")
        print(hasta_dict[id])

    # sözlükteki tüm degerler
    print("Tüm hastalar\n")
    for item in hasta_dict:
        print("hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))

    hasta_bilgilerini_dosyaya_yaz(hasta_dict)

def hasta_bilgilerini_dosyaya_yaz(hasta_dict):

    f = open("14010011015.txt", "w")
    for k, v in hasta_dict.items():
        s = str(k) + "   " + str(v) + "\n"
        b = f.write(s)

    f.close()
    print("Verileriniz dosyanıza kaydedildi.")
    menuden_cikis()


def menuden_cikis():
    tekrar = str(input("\nMenüye geri dönmek isterseniz e,cıkmak icin h ye basın: \n"))
    if (tekrar.lower() == 'e'):
        main()
    else:
        print("\nGüle Güle..Çıkış yaptınız!")
        exit()

def hasta_yatis_masraflari(hasta_dict):

    id = int(input("Yatış masraflarını hesaplamak istediginiz hastanın No'sunu giriniz:"))
    if (id in hasta_dict):
        gunluk_yatis_masrafi = 150
        d1 =  hasta_dict[id]["Yatış Gün Sayısı"]
        toplam_yatis_masrafi = (d1) * (gunluk_yatis_masrafi)
        print(toplam_yatis_masrafi)
    else:
        print("Böyle bir hasta bulunmamaktadır.")


    d3 = {"Yatış Masrafı": toplam_yatis_masrafi}
    hasta_dict[id].update(d3)

    menuden_cikis()

def korona_testi(hasta_dict):
    id = int(input("Korona Testi yaptırmak istediginiz hastanın No'sunu giriniz:"))

    if (id in hasta_dict):

        tanı1 = str(input("\nAteşiniz varsa e,yoksa h ye basın: \n"))
        tanı2 = str(input("\nKuru Öksürüğünüz varsa e,yoksa h ye basın: \n"))
        tanı3 = str(input("\nYorgunlugunuz varsa e,yoksa h ye basın: \n"))

        if (tanı1.lower() == 'e' and tanı2.lower() == 'e' and tanı3.lower() == 'e'):

            korona_sonuc = "pozitif"

            print("Hemen bir sağlık kurulusuna basvurunuz.Maskenizi Cıkarmayınız!Testiniz pozitif!!!!")

            d3 = {"Korona Sonuç": korona_sonuc}
            hasta_dict[id].update(d3)

            for item in hasta_dict:
                print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)

        elif( tanı1.lower() == 'h' and tanı2.lower() == 'e' and tanı3.lower() == 'e' or
             tanı1.lower() == 'e' and tanı2.lower() == 'h' and tanı3.lower() == 'e' or
             tanı1.lower() == 'e' and tanı2.lower() == 'e' and tanı3.lower() == 'h' ) :

            print("Kendinizi dinlendirin. Testiniz negatif. Sosyal mesafenizi koruyun")

            korona_sonuc = "negatif"

            d3 = {"Korona Sonuç": korona_sonuc}
            hasta_dict[id].update(d3)

            for item in hasta_dict:
                print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)

        elif (tanı1.lower() == 'h' and tanı2.lower() == 'h' and tanı3.lower() == 'e' or
              tanı1.lower() == 'e' and tanı2.lower() == 'h' and tanı3.lower() == 'h' or
              tanı1.lower() == 'h' and tanı2.lower() == 'e' and tanı3.lower() == 'h'):

            print("Kendinizi dinlendirin. Testiniz negatif. Sosyal mesafenizi koruyun")

            korona_sonuc = "negatif"

            d3 = {"Korona Sonuç": korona_sonuc}
            hasta_dict[id].update(d3)

            for item in hasta_dict:
                print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)

        elif(tanı1.lower() == 'h' and tanı2.lower() == 'h' and tanı3.lower() == 'h'):

            korona_sonuc = "negatif"

            print("Korkulacak bir durum yoktur.\n Evinizde kalın. \n Sosyal mesafenizi koruyun.\n Maske takmayı ihmal etmeyin.")

            d3 = {"Korona Sonuç": korona_sonuc}
            hasta_dict[id].update(d3)

            for item in hasta_dict:
                print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))
            hasta_bilgilerini_dosyaya_yaz(hasta_dict)

    else:
        print("Böyle bir hasta bulunmamaktadır.")



    for item in hasta_dict:
        print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))
    menuden_cikis()


def hasta_refaktci_sayisi_belirleme(hasta_dict):
    id = int(input("Hastanın refakatcı sayısını belirlemek istediginiz hastanın No'sunu giriniz:"))
    if (id in hasta_dict):
        refakatci_sayisi = int(input("Refakatçi sayısını belirleyiniz.(Tam sayı olarak giriniz:"))
        d3 = {"Refakatci Sayısı": refakatci_sayisi}
        hasta_dict[id].update(d3)
        for item in hasta_dict:
            print("Hasta No'su : {} , Bilgileri : {}".format(item, hasta_dict[item]))
        hasta_bilgilerini_dosyaya_yaz(hasta_dict)
    else:
        print("Böyle bir hasta bulunmamaktadır.")

def main():
    baslik()
    menu()
    secim = secimYap()
    while True:
        if (secim < 13 and secim > 0):
            if (secim == 1):
                if(len(hasta_dict) == 0):
                    hasta_bilgilerini_dosyadan_oku()
                else:
                    hasta_goruntuleme(hasta_dict)

            elif( secim == 2):
                hasta_guncelleme(hasta_dict)

            elif(secim == 3):
                hasta_arama(hasta_dict)

            elif(secim == 4):
                hasta_silme(hasta_dict)

            elif(secim == 5):
                hasta_yatis_suresi(hasta_dict)

            elif(secim == 6):
                hasta_ekleme(hasta_dict)

            elif(secim == 7):
                hasta_bilgilerini_dosyaya_yaz(hasta_dict)

            elif(secim == 8):
                hasta_bilgilerini_dosyadan_oku()

            elif(secim == 9):
                hasta_yatis_masraflari(hasta_dict)

            elif(secim == 10):
                korona_testi(hasta_dict)

            elif(secim == 11):
                hasta_refaktci_sayisi_belirleme(hasta_dict)

            elif(secim == 12):
                menuden_cikis()


        else:
            print("Doğru seçim yapınız")


if __name__ == '__main__':
    main()