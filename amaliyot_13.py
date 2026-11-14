import csv

yonalish = input("Yo'nalish: ").strip()

yaroqli = []

with open("talabalar.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["yonalish"].strip().lower() == yonalish.lower():
            yaroqli.append(row)

yaroqli.sort(key=lambda x: int(x["ball"]), reverse=True)

print(f"{len(yaroqli)} ta talaba topildi.")
print("Natijalar filtrlangan_talabalar.csv fayliga yozildi.")

with open("filtrlangan_talabalar.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ism", "yosh", "yonalish", "ball"])
    writer.writeheader()
    writer.writerows(yaroqli)