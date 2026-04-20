import json # [GÖREV 3] Dosya işlemleri için gerekli kütüphane

# V2 GÖREVLERİ:
# 1. Kişi Silme (İsme göre rehberden çıkarma)
# 2. Kişi Arama (İsme göre hızlı sorgulama)
# 3. Dosya Kaydı (Verilerin rehber.json dosyasına kaydedilmesi ve açılışta yüklenmesi)

def rehberi_kaydet(rehber):
    """[GÖREV 3] Rehberi bir JSON dosyasına kaydeder."""
    with open("rehber.json", "w", encoding="utf-8") as f:
        json.dump(rehber, f, ensure_ascii=False, indent=4)

def rehberi_yukle():
    """[GÖREV 3] Program açıldığında verileri dosyadan okur."""
    try:
        with open("rehber.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def rehber_listele(rehber):
    if not rehber:
        print("\nRehber şu an boş.")
    else:
        sirali_rehber = sorted(rehber, key=lambda x: x['isim'].lower())
        print("\n--- Rehber Listesi (A-Z) ---")
        for kisi in sirali_rehber:
            print(f"İsim: {kisi['isim']} - Tel: {kisi['tel']}")

def main():
    # Program başlarken eski verileri yükle
    rehber = rehberi_yukle()
    
    while True:
        print("\n--- mini-contacts V2 ---")
        print("1. Kişi Ekle\n2. Listele\n3. Kişi Ara\n4. Kişi Sil\n5. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("İsim: ")
            tel = input("Telefon: ")
            if not tel.isdigit():
                print("Hata: Telefon numarası sadece rakamlardan oluşmalıdır!")
            else:
                rehber.append({"isim": isim, "tel": tel})
                rehberi_kaydet(rehber) # Her eklemede kaydet
                print(f"{isim} eklendi.")

        elif secim == "2":
            rehber_listele(rehber)

        elif secim == "3":
            # [GÖREV 2] Kişi Arama
            arama = input("Aranacak isim: ").lower()
            bulunanlar = [k for k in rehber if arama in k['isim'].lower()]
            if bulunanlar:
                print("\n--- Arama Sonuçları ---")
                for k in bulunanlar:
                    print(f"İsim: {k['isim']} - Tel: {k {k['tel']}}")
            else:
                print("Kişi bulunamadı.")

        elif secim == "4":
            # [GÖREV 1] Kişi Silme
            silinecek = input("Silmek istediğiniz kişinin tam ismi: ")
            onay = input(f"{silinecek} kişisini silmek istediğinize emin misiniz? (e/h): ")
            if onay.lower() == 'e':
                yeni_rehber = [k for k in rehber if k['isim'] != silinecek]
                if len(yeni_rehber) < len(rehber):
                    rehber = yeni_rehber
                    rehberi_kaydet(rehber) # Sildikten sonra kaydet
                    print(f"{silinecek} başarıyla silindi.")
                else:
                    print("İsim bulunamadı.")

        elif secim == "5":
            onay = input("Çıkmak istediğinize emin misiniz? (e/h): ")
            if onay.lower() == 'e':
                print("Veriler kaydedildi. Güle güle!")
                break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
