menu = {"lavash": 28000, "somsa": 10000, "choy": 3000}

def buyurtma(*args, **kwargs):
    jami = 0
    print(f"Mijoz: {kwargs.get('mizoj', kwargs.get('mijoz', 'Nomalum'))}")
    print(f"Telefon: {kwargs.get('telefon', 'Nomalum')}")
    
    for mahsulot in args:
        if mahsulot in menu:
            jami += menu[mahsulot]
        else:
            print(f"Ogohlantirish: '{mahsulot}' menuda yoq!")
            
    print(f"Jami: {jami} so'm")

buyurtma("lavash", "choy", "somsa", mijoz="Dilshod", telefon="901234567")