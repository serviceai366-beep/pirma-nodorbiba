print("Biļešu cenas kalkulators")

vecums = int(input("Ievadi savu vecumu: "))

if vecums < 6:
    cena = 0
elif vecums < 17:
    cena = 3
elif vecums < 64:
    cena = 7
elif vecums > 65:
      cena = 4

print(f"Biļetes cena ir {cena} EUR.")
