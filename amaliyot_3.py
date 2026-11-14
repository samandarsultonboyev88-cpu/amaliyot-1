import math

shaharlar = {
    "A": (0, 0),
    "B": (3, 4),
    "C": (6, 8)
}

def masofa(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

kalitlar = list(shaharlar.keys())
max_masofa = -1
eng_uzoq_juftlik = ""

for i in range(len(kalitlar)):
    for j in range(i + 1, len(kalitlar)):
        s1, s2 = kalitlar[i], kalitlar[j]
        dist = masofa(shaharlar[s1], shaharlar[s2])
        print(f"{s1} va {s2}: {dist}")
        if dist > max_masofa:
            max_masofa = dist
            eng_uzoq_juftlik = f"{s1} – {s2} ({dist})"

print(f"Eng uzoq yo'nalish: {eng_uzoq_juftlik}")