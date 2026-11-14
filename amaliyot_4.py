ombor_1 = {"olma": 20, "anor": 12, "nok": 8}
ombor_2 = {"olma": 15, "banan": 10, "nok": 5}

natija = ombor_1.copy()
for mahsulot, miqdor in ombor_2.items():
    natija[mahsulot] = natija.get(mahsulot, 0) + miqdor

print(natija)