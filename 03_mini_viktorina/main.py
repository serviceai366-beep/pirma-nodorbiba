print("Python mini viktorīna")

punkti = 0

atbilde = input("1. Kāds atslēgvārds sāk nosacījumu? ").lower()
if atbilde == "if": 
    print("Krasava")
    punkti += 1

# TODO: pārbaudi pirmo atbildi un palielini punktu skaitu

atbilde = input("2. Kāda funkcija izvada tekstu? ").lower()
if atbilde == "print":
    print("mashina")
    punkti += 1
# TODO: pārbaudi otro atbildi un palielini punktu skaitu

atbilde = input("3. Kāds cikls iet cauri elementiem? ").lower()
if atbilde == "for":
    print("Dimon LOX")
    punkti += 1
# TODO: pārbaudi trešo atbildi un palielini punktu skaitu

print(f"Tu ieguvi {punkti} no 3 punktiem.")