import csv
import matplotlib.pyplot as plt

FILENAME = "kitoblar.csv"

def kitoblarni_korish():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("\n--- Barcha kitoblar ---")
        for row in reader:
            print(f"Nomi: {row['nom']}, Kategoriya: {row['kategoriya']}, Muallif: {row['muallif']}, O'qilgan: {row['oqligan']}")

def kitob_qidirish():
    kalit = input("Qidirilayotgan kitob nomi: ").strip().lower()
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        topildi = False
        for row in reader:
            if kalit in row['nom'].lower():
                print(f"Topildi -> Nomi: {row['nom']}, Kategoriya: {row['kategoriya']}, Muallif: {row['muallif']}, O'qilgan: {row['oqligan']}")
                topildi = True
        if not topildi:
            print("Bunday kitob topilmadi.")

def kategoriya_filtrlash():
    kat = input("Kategoriya nomini kiriting: ").strip().lower()
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print(f"\n--- {kat.capitalize()} kategoriyasidagi kitoblar ---")
        topildi = False
        for row in reader:
            if row['kategoriya'].strip().lower() == kat:
                print(f"- {row['nom']} ({row['muallif']})")
                topildi = True
        if not topildi:
                print("Bu kategoriyada kitob topilmadi.")

def eng_kop_oqilgan_kitob():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        eng_kop = None
        max_qiymat = -1
        for row in reader:
            qiymat = int(row['oqligan'])
            if qiymat > max_qiymat:
                max_qiymat = qiymat
                eng_kop = row
        if eng_kop:
            print(f"\nEng ko'p o'qilgan kitob:\n{eng_kop['nom']}     {eng_kop['oqligan']} marta")

def grafik_chiqarish():
    kategoriyalar = {}
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            kat = row['kategoriya'].strip()
            kategoriyalar[kat] = kategoriyalar.get(kat, 0) + 1
            
    plt.figure(figsize=(8, 5))
    plt.bar(kategoriyalar.keys(), kategoriyalar.values(), color='skyblue')
    plt.xlabel("Kategoriyalar")
    plt.ylabel("Kitoblar soni")
    plt.title("Kategoriyalar bo'yicha kitoblar taqsimoti")
    plt.show()

def kitob_qoshish():
    nom = input("Kitob nomi: ").strip()
    kategoriya = input("Kategoriyasi: ").strip()
    muallif = input("Muallifi: ").strip()
    oqligan = input("O'qilgan soni: ").strip()
    
    with open(FILENAME, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nom, kategoriya, muallif, oqligan])
    print("Yangi kitob muvaffaqiyatli qo'shildi va fayl yangilandi!")

def asosiy():
    while True:
        print("\n1. Kitoblarni ko'rish")
        print("2. Kitob qidirish")
        print("3. Kategoriya bo'yicha filtrlash")
        print("4. Eng ko'p o'qilgan kitob")
        print("5. Grafik chiqarish")
        print("6. Kitob qo'shish")
        print("0. Chiqish")
        
        tanlov = input("Tanlov: ").strip()
        
        if tanlov == "1":
            kitoblarni_korish()
        elif tanlov == "2":
            kitob_qidirish()
        elif tanlov == "3":
            kategoriya_filtrlash()
        elif tanlov == "4":
            eng_kop_oqilgan_kitob()
        elif tanlov == "5":
            grafik_chiqarish()
        elif tanlov == "6":
            kitob_qoshish()
        elif tanlov == "0":
            break
        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring.")

if __name__ == "__main__":
    asosiy()