def bolish(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Faqat son kiritish kerak!"
    return a / b

try:
    son1 = float(input("Birinchi son: "))
    son2 = float(input("Ikkinchi son: "))
    natija = bolish(son1, son2)
    print("Natija:", natija)
except ZeroDivisionError:
    print("Xatolik: Nolga bo'lish mumkin emas. Dastur ishlashda davom etmoqda.")
except (ValueError, AssertionError) as e:
    print(f"Xatolik: {e}. Dastur ishlashda davom etmoqda.")