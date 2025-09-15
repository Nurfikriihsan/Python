import re

email = input("Masukkan email: ")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
trusted_domains = ["gmail.com", "yahoo.com", "outlook.com", "edu", "gov"]

if re.match(pattern, email):
    domain = email.split("@")[1]
    if any(td in domain for td in trusted_domains):
        print("Email valid")
    else:
        print("Email valid tapi domain tidak umum!")
else:
    print("Format email tidak valid!")
