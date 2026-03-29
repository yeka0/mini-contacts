# mini-contacts V1
# Görev 1: Alfabetik Sıralama
# Görev 2: Telefon Numarası Doğrulama (isdigit)
# Görev 3: Çıkış Onayı Mekanizması

def rehber_listele(rehber):
    if not rehber:
        print("\nRehber şu an boş.")
    else:
        # [GÖREV 1] İsimleri A'dan Z'ye sıralıyoruz
        sirali_rehber = sorted(rehber, key=lambda x: x['isim'].lower())
        print("\n--- Rehber Listesi (A-Z) ---")
        for kisi in sirali_rehber:
            print(f"İsim: {kisi['isim']} - Tel: {kisi['tel']}")

def main():
    rehber = []
    while True:
        print("\n1. Kişi Ekle\n2. Listele\n3. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("İsim: ")
            tel = input("Telefon: ")
            
            # [GÖREV 2] Sadece rakam girilip girilmediğini kontrol ediyoruz
            if not tel.isdigit():
                print("Hata: Telefon numarası sadece rakamlardan oluşmalıdır!")
            else:
                rehber.append({"isim": isim, "tel": tel})
                print(f"{isim} eklendi.")

        elif secim == "2":
            rehber_listele(rehber)

        elif secim == "3":
            # [GÖREV 3] Yanlışlıkla çıkışı önlemek için onay alıyoruz
            onay = input("Çıkmak istediğinize emin misiniz? (e/h): ")
            if onay.lower() == 'e':
                print("Güle güle!")
                break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()