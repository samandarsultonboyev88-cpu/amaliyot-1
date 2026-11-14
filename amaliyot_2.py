buyurtmalar = [
    {"mahsulot": "Kitob", "narx": 45000, "miqdor": 2},
    {"mahsulot": "Ruchka", "narx": 5000, "miqdor": 10},
    {"mahsulot": "Sumka", "narx": 180000, "miqdor": 1}
]

eng_qimmat_mahsulot = ""
eng_qimmat_qiymat = -1

for b in buyurtmalar:
    qiymat = b["narx"] * b["miqdor"]
    print(f"{b['mahsulot']}: {qiymat} so'm")
    if qiymat > eng_qimmat_qiymat:
        eng_qimmat_qiymat = qiymat
        eng_qimmat_mahsulot = b["mahsulot"]

print(f"Eng qimmat buyurtma: {eng_qimmat_mahsulot} — {eng_qimmat_qiymat} so'm")