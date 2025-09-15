import re

password = input("Masukkan password: ")

panjang = len(password) >= 8
huruf_besar = re.search(r"[A-Z]", password)
huruf_kecil = re.search(r"[a-z]", password)
angka = re.search(r"\d", password)
simbol = re.search(r"\W", password)

if all([panjang, huruf_besar, huruf_kecil, angka, simbol]):
    print("Password kuat")
else:
    print("Password lemah")
