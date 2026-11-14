import string
from collections import Counter

matn = matn = "Python dasturlash qiziqarli. Python imkoniyatlari keng."

tozalangan = matn.translate(str.maketrans('', '', string.punctuation)).lower()
sozlar = tozalangan.split()

sozlar_soni = len(sozlar)
eng_uzun_soz = max(sozlar, key=len) if sozlar else ""

harflar = [h for h in tozalangan if h != ' ']
eng_kop_harf = Counter(harflar).most_common(1)[0][0] if harflar else ""

soz_sanoq = Counter(sozlar)
takrorlanmaydigan = [s for s, c in soz_sanoq.items() if c == 1]

print(f"So'zlar soni: {sozlar_soni}")
print(f"Eng uzun so'z: {eng_uzun_soz}")
print(f"Eng ko'p uchragan harf: {eng_kop_harf}")
print(f"Takrorlanmaydigan so'zlar: {', '.join(takrorlanmaydigan)}")