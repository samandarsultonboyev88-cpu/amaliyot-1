import json

with open("sozlamalar.json", "r", encoding="utf-8") as f:
    data = json.load(f)

yangi_mavzu = input("Mavzu (light/dark): ").strip()
yangi_bildirishnoma = input("Bildirishnoma (ha/yo'q): ").strip().lower()

data["mavzu"] = yangi_mavzu
data["bildirishnoma"] = True if yangi_bildirishnoma in ("ha", "true", "yes") else False

with open("sozlamalar.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Yangilangan fayl:")
print(json.dumps(data, indent=4))