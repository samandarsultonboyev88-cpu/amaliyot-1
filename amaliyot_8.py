fayllar = ["Hisobot 2026.pdf", "profil_rasmi.jpg", "video.mp4", "jadval.xlsx", "diagramma.png"]

ruxsat = (".pdf", ".jpg", ".png")
yaroqli = []
yaroqsiz = []

for f in fayllar:
    if f.lower().endswith(ruxsat):
        yaroqli.append(f.replace(" ", "_"))
    else:
        yaroqsiz.append(f)

print("Yaroqli:")
for y in yaroqli:
    print(y)

print("\nYaroqsiz:")
for y in yaroqsiz:
    print(y)