
import matplotlib.pyplot as plt

kategoriyalar = ["Texnika", "Kiyim", "Oziq-ovqat"]
savdo = [35, 20, 45]  

plt.bar(kategoriyalar, savdo, align="center", width=0.3, label="Katigoriya savdosi", color="blue")

plt.legend()

plt.title("Tavarlar")

plt.ylabel("dona")

plt.show()

