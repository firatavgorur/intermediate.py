FıratHesap = {

    "ad" : "Fırat Avgörür",
    "hesapNo" : "439884938",
    "bakiye" : 3000,
    "ekHesap": 2000
}

def paraCek():
    tutar = input("\nÇekmek İstediğiniz Tutarı Giriniz: ")
    if int(tutar) > FıratHesap["bakiye"]:
        bakiyeSorgula(FıratHesap)
        soru2 = input("\nBakiyeniz yetersizdir. Ek hesap kullanmak ister misiniz?: ")
        if soru2 == "Evet":
            soru3 = input("\nÇekmek istediğiniz tutarı giriniz? :")
            if int(soru3) > (FıratHesap["bakiye"] + FıratHesap["ekHesap"]):
                print("\nBakiyeniz yetersizdir lütfen geçerli tutar giriniz.")
            else:
                if int(soru3) == (FıratHesap["bakiye"] + FıratHesap["ekHesap"]) or int(soru3) < (FıratHesap["bakiye"] + FıratHesap["ekHesap"]):
                    bakiye = FıratHesap["bakiye"]
                    ekhesapkullanıcakmiktar = int(soru3) - FıratHesap["bakiye"]
                    FıratHesap["bakiye"] = 0
                    FıratHesap["ekHesap"] -= ekhesapkullanıcakmiktar
                    print(f"\nİstediğiniz tutar hazırlanıyor.Kalan bakiyeniz, Ana Hesap : {FıratHesap['bakiye']} TL, Ek Hesap: {FıratHesap['ekHesap']}" )
                    bakiyeSorgula(FıratHesap)
        else:
            print("\nİşleminiz iptal edilmiştir.")
    else:
        if int(tutar) == FıratHesap["bakiye"] or int(tutar) < FıratHesap["bakiye"]:
            FıratHesap["bakiye"] -= int(tutar)
            print("\nParanız Hazırlanıyor..")
            bakiyeSorgula(FıratHesap)


def paraYatir():
    tutar = input("\nYatırmak İstediğiniz Tutarı Giriniz: ")
    if int(tutar) > 0:
        FıratHesap["bakiye"] += int(tutar)
        print("\nParanız ana hesabınıza yatırılıyor.")
        print(f"\nYeni bakiyeniz : {FıratHesap['bakiye']} TL'dir.Ek hesap bakiyeniz {FıratHesap['ekHesap']} TL'dir. Toplam bakiye = {FıratHesap['bakiye'] + FıratHesap['ekHesap']} TL'dir.")
    
    else:
        if int(tutar) <= 0:
            print("\nEksik veya yetersiz tutar girdiniz.")

def bakiyeSorgula(FıratHesap):
    print(f'\n{FıratHesap["hesapNo"]} nolu ana hesabınızda {FıratHesap["bakiye"]} tl bulunmaktadır. Ek hesabınızda ise {FıratHesap["ekHesap"]} tl bulunmaktadır.')


def bakiyeSorgulama():
    print(f"\nMerhaba {FıratHesap['ad']}, {FıratHesap['hesapNo']} nolu ana hesabınızda toplam {FıratHesap['bakiye']} TL bulunmaktadır.")



print("\n************** ATM ***************\n")

print("----    '1' : Para Çekme       ----")  
print("----    '2' : Para Yatırma     ----")
print("----    '3' : Bakiye Sorgulama ----")
print("----    '4' : Çıkış            ----")

print("\n************** ATM ***************\n")

islemSec = input("\nYapmak istediğiniz işlemi seçiniz: ")
if islemSec == "1":
    paraCek()
elif islemSec == "2":
    paraYatir()
elif islemSec == "3":
    bakiyeSorgulama()
else:
    if islemSec == "4":
        print("Hoşçakalın!")
        False

