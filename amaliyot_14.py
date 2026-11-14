from matplotlib import pyplot

oylar = ["Yan", "Fev", "Mar", "Apr", "May", "Iyun"]
daromad = [12, 15, 11, 19, 22, 18] 


pyplot.plot(oylar, daromad, color="red", marker="p", linestyle="-.")

pyplot.title("Oylik daromatlar")
pyplot.xlabel("oylar")
pyplot.ylabel("daromatlar mln som")

pyplot.grid(True)

pyplot.savefig("natijalar.png")

pyplot.show()



