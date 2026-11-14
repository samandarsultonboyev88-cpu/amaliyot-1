import csv

daromadlar = {}

with open("savdo.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        kategoriya = row["kategoriya"].strip()
        tushum = int(row["narx"]) * int(row["miqdor"])
        daromadlar[kategoriya] = daromadlar.get(kategoriya, 0) + tushum

eng_daromadli = ""
max_tushum = -1

for kat, tushum in daromadlar.items():
    print(f"{kat}: {tushum:,} so'm".replace(",", " "))
    if tushum > max_tushum:
        max_tushum = tushum
        eng_daromadli = kat

print(f"Eng daromadli kategoriya: {eng_daromadli}")