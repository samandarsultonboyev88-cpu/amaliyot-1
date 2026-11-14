natijalar = [
    {"ism": "Aziza", "ball": 82},
    {"ism": "Jasur", "ball": 64},
    {"ism": "Madina", "ball": 91},
    {"ism": "Sardor", "ball": 70}
]

yuqori = list(filter(lambda x: x["ball"] > 70, natijalar))
print("70 dan yuqori:", ", ".join([x["ism"] for x in yuqori]))

oshirilgan = list(map(lambda x: round(x["ball"] * 1.1, 1), yuqori))
print("10% oshirilgan ballar:", oshirilgan)

saralangan = sorted(yuqori, key=lambda x: x["ball"] * 1.1, reverse=True)
print("Saralangan:", ", ".join([x["ism"] for x in saralangan]))